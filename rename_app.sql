UPDATE django_content_type SET app_label='mobility' WHERE app_label='countries'

ALTER TABLE countries_country RENAME TO mobility_country;
ALTER TABLE countries_mobility RENAME TO mobility_mobility;
ALTER TABLE countries_institution RENAME TO mobility_institution;
ALTER TABLE countries_mobilitycalendar RENAME TO mobility_mobilitycalendar;
ALTER TABLE countries_mobilitydone RENAME TO mobility_mobilitydone;
ALTER TABLE countries_myuser RENAME TO mobility_myuser;
ALTER TABLE countries_myuser_groups RENAME TO mobility_myuser_groups;
ALTER TABLE countries_myuser_user_permissions RENAME TO mobility_myuser_user_permissions;
ALTER TABLE countries_person RENAME TO mobility_person;
ALTER TABLE countries_result RENAME TO mobility_result;
ALTER TABLE countries_yearresult RENAME TO mobility_yearresult;

UPDATE django_migrations SET app='mobility' WHERE app='countries';