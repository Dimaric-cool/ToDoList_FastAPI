-- +goose Up
-- +goose StatementBegin
-- Добавляем колонку tags в таблицу todo (массив строк)
ALTER TABLE todo ADD COLUMN tags TEXT[] DEFAULT '{}';
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
-- Удаляем колонку tags
ALTER TABLE todo DROP COLUMN IF EXISTS tags;
-- +goose StatementEnd