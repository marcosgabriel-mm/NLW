from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class CheckInRepository:
    def insert_check_in(self, attendee_id: str) -> str:
        with db_connection_handler as database:
            try:
                check_in = (
                    CheckIns(attendeeId = attendee_id)
                )
                
                database.session.add(check_in)
                database.session.commit()
                
                return check_in
            
            except IntegrityError:
                raise Exception("Check-in já cadastrado")


            except Exception as exception:
                db_connection_handler.session.rollback()
                raise exception