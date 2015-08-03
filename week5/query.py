"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
brand = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
corvettes = Model.query.filter_by(name='Corvette',brand_name='Chevrolet').all()


# Get all models that are older than 1960.
pre1960s = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
post1920s = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
ors = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
notdisc1903 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
discorpre1950 = Brand.query.filter(db.or_(Brand.discontinued.isnot(None), Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
notchevy = Model.query.filter(Model.brand_name.isnot("Chevrolet")).all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = db.session.query(Model, Brand).filter(Model.year == year).join(Brand)

    for model, brand in models.all():
    	print model.name, model.brand_name, brand.headquarters

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = db.session.query(Brand, Model).join(Model)

    for brand, model in brands.all():
     	print brand.name, model.name



    

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
	brands_list = []
    brands = Brand.query.filter(db.or_(Brand.name == mystr, Brand.name.like('%'+mystr+'%')))
    for brand in brands.all():
    	brands_list.append(brand)
    print brands_list


def get_models_between(start_year, end_year):
    models_list = []
    models = Model.query.filter(Model.year > start_year, Model.year < end_year)
    for model in models.all():
    	models_list.append(model)
    print models_list
    	

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
#Answer the value is a query that Python translates into something SQLite can understand. 
#The datatype is a SQLAlchemy base query class which inherits from SQLAlchemy model.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
#Answer: An association table is a table which links/bridges two related tables.
#The association table creates a one-to-many relationship with each of the related tables.
#Without the association table, the two related tables would rely on many-to-many relationship 
#to link them, which is not supported by SQL, and causes massive headaches when other programs do.
