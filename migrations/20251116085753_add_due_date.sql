-- +goose Up
-- +goose StatementBegin
-- Добавляем колонку due_date в таблицу todo
ALTER TABLE todo ADD COLUMN due_date DATE;

-- Создаем индекс для оптимизации запросов по due_date
CREATE INDEX IF NOT EXISTS idx_todo_due_date ON todo(due_date);
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
-- Удаляем индекс
DROP INDEX IF EXISTS idx_todo_due_date;

-- Удаляем колонку due_date
ALTER TABLE todo DROP COLUMN IF EXISTS due_date;
-- +goose StatementEnd