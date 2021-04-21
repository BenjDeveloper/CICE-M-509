declare
    i number (8) := 1;
begin
    while (i<=10)
    loop
        DMBS_OUTPUT.PUT_LINE(i);
        i := i+1;
    end loop;
end;
