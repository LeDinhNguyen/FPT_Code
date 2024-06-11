CREATE TABLE  Book (
    book_id INT  PRIMARY KEY,
    title VARCHAR(255) DEFAULT NULL,
    edition INT DEFAULT 0,
    year int,
    price DECIMAL (10, 2) NOT NULL,
    issn VARCHAR(20),
    pages INT  NOT NULL,
    aisle INT DEFAULT 0,
    description TEXT DEFAULT NULL
);
INSERT INTO book (book_id, title ,edition, year, price, issn, pages, aisle, description) VALUES (1,'The Catcher in the Rye', 13, 2009, 4.58, '1-234-5678-90', 280, 15,  'This is a book about a boy and his adventures.');
INSERT INTO book (book_id,title, edition, year, price, issn, pages, aisle, description) VALUES (2,'The Great Gatsby', 34, 2013, 7.95, '9-876-543-210-90', 130, 18,  'This is a story about love, wealth and deception.');
INSERT INTO book (book_id,title, edition, year, price, issn, pages, aisle, description) VALUES (3,'To Kill a Mockingbird', 24, 1960, 8.57, '3-456-789-012-34', 210, 17, 'This is a book about racism and the power of empathy.');
INSERT INTO book (book_id,title, edition, year, price, issn, pages, aisle, description) VALUES (4,'The Grapes of Wrath', 30, 1976, 5.28, '4-567-890-123-45', 340, 13,  'This is a book about family and resilience.');
INSERT INTO book (book_id,title, edition, year, price, issn, pages, aisle, description) VALUES (5,'The Scarlet Letter', 25, 1987, 6.34, '5-678-901-234-56', 200, 20,  'This is a book about the power of shame.');
INSERT INTO book (book_id,title, edition, year, price, issn, pages, aisle, description) VALUES (6,'The Old Man and the Sea', 37, 1982, 5.42, '6-789-012-345-67', 180, 16, 'This is a book about an aging fisherman and his quest for redemption.');
INSERT INTO book (book_id,title, edition, year, price, issn, pages, aisle, description) VALUES (7,'The Sun Also Rises', 18, 1967, 6.45, '7-890-123-456-78', 220, 21, 'This is a book about the search for meaning and identity.');
INSERT INTO book (book_id,title, edition, year, price, issn, pages, aisle, description) VALUES (8,'The Great Gatsby', 34, 2013, 7.95, '9-876-543-210-90', 130, 18, 'This is a story about love, wealth and deception.');
INSERT INTO book (book_id,title, edition, year, price, issn, pages, aisle, description) VALUES (9,'To Kill a Mockingbird', 24, 1960, 8.57, '3-456-789-012-34', 210, 17,  'This is a book about racism and the power of empathy.');

select * from Book;

select book_id, title from Book;

select book_id, title from Book
where book_id = '1';

select book_id,title from Book
where title like 'To%';

select title, pages from Book
where pages >= 210 and pages <= 340;

select * from Book
where price in (4.58, 8.57);

select title from Book
order by title;

select	title, pages from Book
order by 2;

select distinct(year) from Book;

select count(aisle) as 'Number of aisle' from Book
group by aisle;

select count(aisle) as 'Number of aisle' from Book
group by aisle
having count(aisle) > 1;

select sum(price) from Book;

select sum(price) as 'Total Sum of Price' from Book;

select max(edition) from Book;

select min(book_id) from Book
where aisle = '15';

select avg(price) from Book
where edition>30;

select ROUND(avg(price),1) from Book;

select len(title) from Book;

select * from Book
where price = (select max(price) from Book);

select * from Book
where price > avg(price);

