from datetime import datetime

from models.model import engine, Base, Session
from models.customer import Customer, CustomerSchema
from models.loan import Loan, LoanSchema





Base.metadata.create_all(engine)

# start session
session = Session()

# create customers
tito_magero = Customer("tito magero", "+233209216257", "accra", "adenta", "east", "102, 342")
nana_ama = Customer("nana ama", "+233200812458", "accra", "adenta", "east", "102, 342")
cynthia_gouanfo = Customer("cynthia gouanfo", "+233200222222", "accra", "kasua", "east", "201, 402.4")
daouda_soumahoro = Customer("daouda soumahoro", "+22543689452", "abidjan", "cocody", "south", "109, 304")
brandon_odiwuor = Customer("brandon odiwuor", "+254200222222", "nairobi", "langata", "center", "203, 192")
alex_njoroge = Customer("alex njoroge", "+254233333333", "nairobi", "westlands", "east", "102, 310")
sabelo_dube = Customer("sabelo dube", "+254443203333", "johannesbourg", "soweto", "north", "201, 301")
genesis_nchoupereu = Customer("genesis nchoupereu", "+254200333333", "accra", "adenta","east", "201, 301")

# create loans
loan_magero = Loan(200, 30, datetime(2020, 5, 17), datetime.now(), customer=tito_magero)
loan_tito = Loan(200, 200, datetime(2019, 12, 5), datetime.now(), customer=tito_magero)
loan_nana = Loan(1000, 800, datetime(2020, 5, 17), datetime.now(), customer=nana_ama)
loan_ama = Loan(1000, 1000, datetime(2019, 12, 5), datetime.now(), customer=nana_ama)
loan_cynthia = Loan(12000, 5000, datetime(2020, 5, 17), datetime.now(), customer=cynthia_gouanfo)
loan_gouanfo = Loan(12000, 12000, datetime(2019, 5, 17), datetime.now(), customer=cynthia_gouanfo)
loan_daouda = Loan(120, 80, datetime(2020, 5, 17), datetime.now(), customer=daouda_soumahoro)
loan_soumahoro = Loan(120, 120, datetime(2019, 12, 5), datetime.now(), customer=daouda_soumahoro)
loan_brandon = Loan(300, 100, datetime(2020, 5, 17), datetime.now(), customer=brandon_odiwuor)
loan_odiwuor = Loan(300, 300, datetime(2019, 12, 5), datetime.now(), customer=brandon_odiwuor)
loan_alex = Loan(240, 70, datetime(2020, 5, 17), datetime.now(), customer=alex_njoroge)
loan_njoroge = Loan(240, 240, datetime(2019, 12, 5), datetime.now(), customer=alex_njoroge)
loan_sabelo = Loan(300, 70, datetime(2020, 5, 17), datetime.now(), customer=sabelo_dube)
loan_dube = Loan(300, 300, datetime(2019, 12, 5), datetime.now(), customer=sabelo_dube)
loan_genesis = Loan(500, 400, datetime(2020, 5, 17), datetime.now(), customer=genesis_nchoupereu)
loan_nchoupereu = Loan(500, 500, datetime(2020, 5, 17), datetime.now(), customer=genesis_nchoupereu)

# Persist data
session.add(tito_magero)
session.add(nana_ama)
session.add(cynthia_gouanfo)
session.add(daouda_soumahoro)
session.add(brandon_odiwuor)
session.add(alex_njoroge)
session.add(sabelo_dube)
session.add(genesis_nchoupereu)

session.add(loan_tito)
session.add(loan_magero)
session.add(loan_nana)
session.add(loan_ama)
session.add(loan_cynthia)
session.add(loan_gouanfo)
session.add(loan_daouda)
session.add(loan_soumahoro)
session.add(loan_brandon)
session.add(loan_odiwuor)
session.add(loan_alex)
session.add(loan_njoroge)
session.add(loan_sabelo)
session.add(loan_dube)
session.add(loan_genesis)
session.add(loan_nchoupereu)




# Write and close database connection.
session.commit()
session.close()