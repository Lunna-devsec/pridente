from sqlalchemy.orm import Session
from modelos import User
import classes
#importar classes
#importar modelos do banco_modelos

class RUser():
    def __init__(self, db: Session):
        self.db = db

    def criar(self, user: classes.User):
        db_user = User(id = user.id,
                                nome = user.nome,
                                senha = user.senha,
                                saldo = user.saldo)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def listar(self):
        users = self.db.query(User).all()
        return users

    def delete(self):
        pass
    def testar():
        print('hello Lunna')