from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from models import Recipe, Ingredient, Category

async def get_recipes_by_ingredient(
    db: AsyncSession,
    ingredient_name: str
) -> List[Recipe]:
    # Use exists subquery to efficiently search recipes with this ingredient
    stmt = (
        select(Recipe)
        .join(Recipe.ingredients)
        .where(Ingredient.name.ilike(ingredient_name))
        .options(selectinload(Recipe.ingredients), selectinload(Recipe.category))
        .order_by(Recipe.id)
    )
    result = await db.execute(stmt)
    return result.scalars().unique().all()

async def get_recipes_by_category(
    db: AsyncSession,
    category_name: str
) -> List[Recipe]:
    stmt = (
        select(Recipe)
        .join(Recipe.category)
        .where(Category.name.ilike(category_name))
        .options(selectinload(Recipe.ingredients), selectinload(Recipe.category))
        .order_by(Recipe.id)
    )
    result = await db.execute(stmt)
    return result.scalars().unique().all()

async def get_recipes_by_ingredient_and_category(
    db: AsyncSession,
    ingredient_name: str,
    category_name: str
) -> List[Recipe]:
    stmt = (
        select(Recipe)
        .join(Recipe.ingredients)
        .join(Recipe.category)
        .where(Ingredient.name.ilike(ingredient_name))
        .where(Category.name.ilike(category_name))
        .options(selectinload(Recipe.ingredients), selectinload(Recipe.category))
        .order_by(Recipe.id)
    )
    result = await db.execute(stmt)
    return result.scalars().unique().all()

async def get_recipe(db: AsyncSession, recipe_id: int) -> Optional[Recipe]:
    stmt = (
        select(Recipe)
        .where(Recipe.id == recipe_id)
        .options(selectinload(Recipe.ingredients), selectinload(Recipe.category))
    )
    result = await db.execute(stmt)
    return result.scalars().first()