-- +goose Up
-- +goose StatementBegin
CREATE TABLE IF NOT EXISTS todo (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    completed BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Создание индексов для оптимизации
CREATE INDEX IF NOT EXISTS idx_todo_title ON todo(title);
CREATE INDEX IF NOT EXISTS idx_todo_completed ON todo(completed);
CREATE INDEX IF NOT EXISTS idx_todo_created_at ON todo(created_at);

-- Комментарии к таблице и колонкам
COMMENT ON TABLE todo IS 'Таблица для хранения задач пользователей';
COMMENT ON COLUMN todo.id IS 'Уникальный идентификатор задачи';
COMMENT ON COLUMN todo.title IS 'Заголовок задачи (обязательное поле)';
COMMENT ON COLUMN todo.description IS 'Подробное описание задачи';
COMMENT ON COLUMN todo.completed IS 'Статус выполнения задачи (false - не выполнена, true - выполнена)';
COMMENT ON COLUMN todo.created_at IS 'Дата и время создания задачи';
COMMENT ON COLUMN todo.updated_at IS 'Дата и время последнего обновления задачи';
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
-- Удаление таблицы (для отката миграции)
DROP TABLE IF EXISTS todo CASCADE;
-- +goose StatementEnd