-- +goose Up
-- +goose StatementBegin
-- Удаляем все существующие задачи
DELETE FROM todo;

-- Делаем колонку user_id обязательной
ALTER TABLE todo ALTER COLUMN user_id SET NOT NULL;
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
-- Делаем колонку nullable обратно
ALTER TABLE todo ALTER COLUMN user_id DROP NOT NULL;
-- +goose StatementEnd