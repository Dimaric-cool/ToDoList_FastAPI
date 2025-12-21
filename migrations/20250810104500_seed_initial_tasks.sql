-- +goose Up
-- +goose StatementBegin
-- Добавление тестовых задач в таблицу todo
INSERT INTO todo (title, description, completed, created_at, updated_at) VALUES
(
    'Первая задача',
    'Описание первой задачи',
    false,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP + INTERVAL '15 minutes'
),
(
    'Вторая задача',
    'Описание второй задачи',
    true,
    CURRENT_TIMESTAMP + INTERVAL '10 minutes',
    CURRENT_TIMESTAMP + INTERVAL '12 minutes'
);
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
-- Удаление тестовых задач
DELETE FROM todo WHERE title IN ('Первая задача', 'Вторая задача');
-- +goose StatementEnd
