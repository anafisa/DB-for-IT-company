CREATE TABLE anfisa(
    discipline text,
    hours int,
    id int
);


INSERT INTO  anfisa(DISCIPLINE, HOURS, ID)
VALUES ('MATH', 7, 05),
        ('INFO', 10, 01);

INSERT INTO  anfisa(DISCIPLINE, HOURS, ID)
VALUES ('PHI', 0, 07),
        ('BIO', 1, 007);

DELETE FROM anfisa WHERE dicipline='MATH';

SELECT hours
FROM anfisa;

DROP TABLE anfisa;
