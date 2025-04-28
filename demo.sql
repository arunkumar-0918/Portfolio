create function demo (
    in p_id int,
    in p_name varchar(255),
    in p_age int
)
returns int
begin 
    declare id int,
            name varchar(255),
            age int;
    select id, name, age into id, name, age from demo where id = p_id;
    if id is null then
        insert into demo (id, name, age) values (p_id, p_name, p_age);
    else
        update demo set name = p_name, age = p_age where id = p_id;
    end if;
    return id;
end;    

demo(1, 'John Doe', 30);