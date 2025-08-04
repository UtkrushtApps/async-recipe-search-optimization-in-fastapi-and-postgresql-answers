# Solution Steps

1. Design a normalized PostgreSQL schema with three main entities: recipes, ingredients, and categories. Model the recipes-to-ingredients relationship as a many-to-many association using a join table, and recipes-to-category as a many-to-one foreign key.

2. In the schema, enforce constraints for uniqueness on category and ingredient names, use foreign keys, and add indexes on names and keys for search/filter efficiency.

3. Implement the SQLAlchemy ORM models reflecting this normalized schema with correct relationships, indexes, and constraints using async-compatible style (no blocking code).

4. Write an Alembic migration that creates the optimized, normalized tables with all constraints and indexes (for PostgreSQL).

5. Configure the async SQLAlchemy engine and sessionmaker in 'database.py', using sessionmaker with AsyncSession. Provide a get_session dependency for FastAPI injection.

6. Implement async CRUD/query functions in 'crud.py'. Use efficient SQLAlchemy async query patterns with select/join options leveraging relationship preloading (selectinload) to avoid N+1 problems. All queries must use await and not block the event loop.

7. For ingredient or category search, implement async SQLAlchemy queries that efficiently JOIN and filter based on indexed columns, returning complete recipe data (eager loading category and ingredients).

8. NO blocking or synchronous database access should be present anywhere in your code. All DB interactions (CRUD/search/filter) must use async SQLAlchemy and asyncpg driver.

