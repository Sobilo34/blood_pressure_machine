from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Sequence, event
from datetime import datetime

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True  # Mark this class as abstract

    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
        Initialize the base model
        """
        super().__init__(*args, **kwargs)
        if not self.id:
            self.id = None
        if not self.created_at:
            self.created_at = datetime.utcnow()
        if not self.updated_at:
            self.updated_at = datetime.utcnow()

    def save(self):
        """
        Save the model to the database
        """
        from models import storage
        storage.new(self)
        storage.save()

    def delete(self):
        """
        Delete the model from the database
        """
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """
        Return a dictionary representation of the model
        """
        model_dict = self.__dict__.copy()
        model_dict.pop('_sa_instance_state', None)
        return model_dict

# Define a listener to ensure the table exists with the correct schema
def ensure_columns(mapper, connection, target):
    table = target.__table__
    columns = [col.name for col in table.columns]
    if 'created_at' not in columns or 'updated_at' not in columns:
        table.append_column(Column('created_at', TIMESTAMP, nullable=False, default=datetime.utcnow))
        table.append_column(Column('updated_at', TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow))
        table.create(connection)

event.listen(BaseModel, 'before_insert', ensure_columns)
