-- +goose Up
-- +goose StatementBegin
-- Добавляем колонку user_id в таблицу todo
ALTER TABLE todo ADD COLUMN user_id INTEGER;

-- Создаем внешний ключ для связи с таблицей users
ALTER TABLE todo ADD CONSTRAINT fk_todo_user_id 
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;

-- Создаем индекс для оптимизации запросов по user_id
CREATE INDEX IF NOT EXISTS idx_todo_user_id ON todo(user_id);

-- Добавляем комментарий к новой колонке
COMMENT ON COLUMN todo.user_id IS 'ID пользователя, которому принадлежит задача';

-- Временно делаем колонку nullable для существующих записей
-- Позже мы обновим существующие задачи и сделаем колонку NOT NULL
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
-- Удаляем внешний ключ
ALTER TABLE todo DROP CONSTRAINT IF EXISTS fk_todo_user_id;

-- Удаляем индекс
DROP INDEX IF EXISTS idx_todo_user_id;

-- Удаляем колонку user_id
ALTER TABLE todo DROP COLUMN IF EXISTS user_id;
-- +goose StatementEnd
