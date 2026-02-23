-- diagnoses
CREATE TABLE diagnoses (
    diagnosis_code VARCHAR(3) PRIMARY KEY,
    description TEXT
);

-- patients
CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    gender VARCHAR(1),
    birthdate DATE
);

-- encounters
CREATE TABLE encounters (
    encounter_id INT PRIMARY KEY,
    patient_id INT,
    visit_date DATE,
    department TEXT,
    diagnosis_code VARCHAR(3),
    CONSTRAINT fk_patient
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    CONSTRAINT diagnoses_fk
    FOREIGN KEY (diagnosis_code) REFERENCES diagnoses(diagnosis_code)
);
