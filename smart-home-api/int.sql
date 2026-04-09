CREATE TABLE sensors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL
);

INSERT INTO sensors (name, location) VALUES ('Thermostat 1', 'Living Room');
INSERT INTO sensors (name, location) VALUES ('Outdoor Sensor', 'Garden');