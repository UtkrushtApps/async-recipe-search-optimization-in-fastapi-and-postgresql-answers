from sqlalchemy import Column, Integer, String, ForeignKey, Index, Table, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.schema import UniqueConstraint

Base = declarative_base()

# Association table for recipe <-> ingredient (many-to-many)
recipe_ingredient_table = Table(
    'recipe_ingredient',
    Base.metadata,
    Column('recipe_id', ForeignKey('recipes.id', ondelete='CASCADE'), primary_key=True),
    Column('ingredient_id', ForeignKey('ingredients.id', ondelete='CASCADE'), primary_key=True),
    # Index for searches by ingredient
    Index('ix_recipe_ingredient_ingredient_id', 'ingredient_id')
)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False, index=True)
    
    recipes = relationship('Recipe', back_populates='category')

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    
    recipes = relationship(
        'Recipe',
        secondary=recipe_ingredient_table,
        back_populates='ingredients'
    )

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False, index=True)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='SET NULL'), index=True)

    category = relationship('Category', back_populates='recipes')
    ingredients = relationship(
        'Ingredient',
        secondary=recipe_ingredient_table,
        back_populates='recipes'
    )

    __table_args__ = (
        Index('ix_recipes_category_id', 'category_id'),
        Index('ix_recipes_title', 'title'),
    )
