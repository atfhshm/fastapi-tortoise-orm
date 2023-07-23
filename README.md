# FastAPI project starter with tortoise orm

## Database migration with aerich

- Creating the migrations folder and pyproject.toml config file.
  ```sh
  aerich init -t db.config.DATABASE_CONFIG
  ```
- Initializing the database
  ```sh
  aerich init-db
  ```
- Migrate the database change
  ```sh
  aerich migrate
  ```
- Upgrade
  ```sh
  aerich upgrade
  ```
