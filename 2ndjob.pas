program MyCalculator;
var
  no_1, no_2: Real;    
  mark: String;           
  output: Real;           

begin
  write('enter the 1st number: ');
  readln(no_1);
  
  write('enter the 2nd number: ');
  readln(no_2);
  
  write('what is the mark(+,-,/,*): ');
  readln(mark);

  if mark = '+' then
    output := no_1 + no_2
  else if mark = '-' then
    output := no_1 - no_2
  else if mark = '/' then
    begin
      if no_2 <> 0 then
        output := no_1 / no_2
      else
        begin
          writeln('Error: Cannot divide by zero!');
          exit;
        end;
    end
  else if mark = '*' then
    output := no_1 * no_2
    else
      begin
        writeln('Error: Invalid operator!');
        exit;
      end;
  writeln('answer: ', output:0:2); 
  readln; 
end.