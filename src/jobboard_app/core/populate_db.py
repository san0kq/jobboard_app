import psycopg2
from decouple import config

conn = psycopg2.connect(
    dbname=config('DB_NAME'),
    host=config('DB_HOST'),
    user=config('DB_USER'),
    password=config('DB_PASSWORD'),
    port='5432',
)
cursor = conn.cursor()

cursor.execute("INSERT INTO accounts_gender (name) VALUES ('Male'), ('Female');")
cursor.execute(
    "INSERT INTO accounts_language (name) VALUES "
    "('English'), ('Russian'), ('Belorusian'), ('Ukraine'), "
    "('Chinese'), ('Poland'), ('German'), ('Italy'), ('France');"
)
cursor.execute(
    "INSERT INTO accounts_languagelevel (name) VALUES "
    "('Elementary(A1)'), ('Pre-Intermediate(A2)'), ('Intermediate(B1)'), "
    "('Upper-Intermediate(B2)'), ('Advanced(C1)'), ('Native(C2)');"
)
cursor.execute(
    "INSERT INTO accounts_tag (name) VALUES "
    "('Python'), ('Java'), ('JS'), ('HTML/CSS'), "
    "('Git'), ('SQL'), ('Django'), ('Web Development');"
)
cursor.execute(
    "INSERT INTO accounts_workformat (name) VALUES "
    "('Remote'), ('Office'), ('Hybrid'), ('Full-time'), ('Part-time'), ('Freelance');"
)
cursor.execute(
    "INSERT INTO accounts_status (name) VALUES "
    "('Open to work'), ('Open for proposals'), ('Not open for proposals'), "
    "('Created'), ('Viewed'), ('Rejected'), ('Accepted for work');"
)
cursor.execute(
    "INSERT INTO accounts_country (name) VALUES "
    "('Belarus'), ('Poland'), ('Ukrain'), ('Russia'), ('USA');"
)
conn.commit()
cursor.execute(
    "INSERT INTO accounts_city (name, country_id) VALUES "
    "('Minsk', 1), ('Warsaw', 2), ('Kiev', 3), ('Moscow', 4), ('Washington', 5);"
)
cursor.execute(
    "INSERT INTO accounts_contract (name) VALUES "
    "('B2B'), ('Employment contract'), ('Mandate contract');"
)
cursor.execute(
    "INSERT INTO accounts_level (name) VALUES " "('Junior'), ('Middle'), ('Senior');"
)
cursor.execute(
    "INSERT INTO accounts_salary (min_salary, max_salary) VALUES "
    "(NULL, 3000.00), (3000.00, 5000.00), (5000.00, NULL);"
)
conn.commit()
cursor.execute(
    "INSERT INTO accounts_profile ("
    "user_id, "
    "phone_number, "
    "birthday, "
    "resume, "
    "years_exp, "
    "city_id, "
    "contract_id, "
    "gender_id, "
    "level_id, "
    "salary_id, "
    "status_id, "
    "work_format_id) VALUES "
    "(1, '+375336473222', '14.11.1994', 'Default resume', 1, 1, 1, 1, 1, 1, 1, 1);"
)
conn.commit()
cursor.execute(
    "INSERT INTO accounts_profilelanguage (profile_id, language_id, language_level_id) "
    "VALUES (1, 1, 2), (1, 2, 6), (1, 3, 6);"
)
cursor.execute("INSERT INTO core_rating (name) VALUES " "('Like'), ('Dislike');")
cursor.execute(
    "INSERT INTO core_position (name) VALUES "
    "('Owner'), ('Recruiter'), ('Project Manager'), ('Delivery Manager');"
)
cursor.execute(
    "INSERT INTO core_adress (city_id, street, house_number, office_number) VALUES "
    "(1, 'Nezalezhnasti', 2, 66), (2, 'Zabraniecka', 33, NULL), "
    "(3, 'Ivana Franko', 22, 3), (4, 'Lenina', 22, 77), (5, '16th St NW', 4, NULL);"
)
cursor.execute(
    "INSERT INTO core_employeesnumber (size_range) VALUES "
    "('up to 50'), ('51-100'), ('101-500'), ('up to 1000'), ('from 1000');"
)
cursor.execute(
    "INSERT INTO core_sector (name) VALUES "
    "('Web'), ('Mobile'), ('AI'), ('Telecommunications');"
)
conn.commit()
cursor.execute(
    "INSERT INTO core_company ("
    "name, "
    "founded_in, "
    "description, "
    "email, "
    "phone_number, "
    "web_site, "
    "adress_id, "
    "employees_number_id, "
    "registred_at, "
    "updated_at) VALUES "
    "('WWW WensCompany', "
    "2004, "
    "'Default description', "
    "'wencompany@gmail.com', "
    "'8033233322', "
    "'www.wencco.com', "
    "5, "
    "5, "
    "CURRENT_TIMESTAMP, "
    "CURRENT_TIMESTAMP), "
    "('AYZH HEXOR', "
    "2000, "
    "'Default description', "
    "'Ayzh@gmail.com', "
    "'88773322223', "
    "'www.hexor.com', "
    "4, "
    "3, "
    "CURRENT_TIMESTAMP, "
    "CURRENT_TIMESTAMP);"
)
conn.commit()
cursor.execute(
    "INSERT INTO core_employee ("
    "first_name, "
    "last_name, "
    "email, "
    "phone_number, "
    "password, "
    "city_id, "
    "company_id, "
    "registred_at, "
    "updated_at) VALUES "
    "('John', "
    "'Cook', "
    "'Cookjohn@gmail.com', "
    "'803326663', "
    "'qwerty', "
    "5, "
    "1, "
    "CURRENT_TIMESTAMP, "
    "CURRENT_TIMESTAMP), ("
    "'Alex', "
    "'Kiganov', "
    "'Kiganov@mail.ru', "
    "'+37566772233', "
    "'qwerty', "
    "4, "
    "2, "
    "CURRENT_TIMESTAMP, "
    "CURRENT_TIMESTAMP);"
)
conn.commit()
cursor.execute(
    "INSERT INTO core_vacancy ("
    "name, "
    "description, "
    "company_id, "
    "employee_id, "
    "salary_id, "
    "years_exp, "
    "registred_at, "
    "updated_at) VALUES "
    "('Python Developer', 'Description', 1, 1, 1, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP), "
    "('Java Developer', 'Description', 2, 2, 2, 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
)
conn.commit()
cursor.execute(
    "INSERT INTO core_review (text, company_id, user_id, created_at, updated_at) VALUES "
    "('Random text', 1, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP), "
    "('Random text', 2, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
)
cursor.execute(
    "INSERT INTO core_reviewrating (rating_id, review_id, user_id, created_at, updated_at) VALUES "
    "(1, 1, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP), "
    "(2, 2, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
)
cursor.execute(
    "INSERT INTO core_sociallink (platform, url, company_id, profile_id) VALUES "
    "('Facebook', 'www.facebook.com/id233323', NULL, 1), "
    "('Github', 'www.github.com/2333232', 1, NULL);"
)
cursor.execute(
    "INSERT INTO core_response ("
    "text, "
    "phone_number, "
    "resume, "
    "status_id, "
    "user_id, "
    "vacancy_id, "
    "created_at, "
    "updated_at) VALUES "
    "('Random text', "
    "'8033233366', "
    "'Random resume', "
    "4, "
    "1, "
    "1, "
    "CURRENT_TIMESTAMP, "
    "CURRENT_TIMESTAMP), "
    "('Random text', "
    "'8023332233', "
    "'Random resume', "
    "5, "
    "1, "
    "2, "
    "CURRENT_TIMESTAMP, "
    "CURRENT_TIMESTAMP);"
)
cursor.execute(
    "INSERT INTO accounts_profile_tags (profile_id, tag_id) VALUES "
    "(1, 1), (1, 2), (1, 3);"
)
cursor.execute(
    "INSERT INTO core_company_sectors (company_id, sector_id) VALUES " "(1, 1), (2, 2);"
)
cursor.execute(
    "INSERT INTO core_employee_positions (employee_id, position_id) VALUES "
    "(1, 1), (2, 2);"
)
cursor.execute(
    "INSERT INTO core_vacancy_contracts (vacancy_id, contract_id) VALUES "
    "(1, 1), (2, 2), (1, 2), (2, 3);"
)
cursor.execute(
    "INSERT INTO core_vacancy_countries (vacancy_id, country_id) VALUES "
    "(1, 1), (1, 2), (2, 1), (2, 3);"
)
cursor.execute(
    "INSERT INTO core_vacancy_levels (vacancy_id, level_id) VALUES "
    "(1, 1), (1, 2), (2, 3);"
)
cursor.execute(
    "INSERT INTO core_vacancy_tags (vacancy_id, tag_id) VALUES "
    "(1, 1), (1, 5), (1, 6), (2, 2), (2, 3), (2, 5);"
)
cursor.execute(
    "INSERT INTO core_vacancy_work_formats (vacancy_id, workformat_id) VALUES "
    "(1, 1), (1, 2), (2, 1), (2, 2), (2, 3);"
)

conn.commit()
conn.close()
