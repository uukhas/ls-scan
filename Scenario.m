Needs@"DatabaseLink`";

BeginPackage@"Scenario`";

connect::usage = "
@brief Connects a SQLite database.
@param name A full or relative name of a database to load.";

get::usage = "
@brief Extracts requred column combinations from connected SQLite database.
@param combinations A set of column combinations to be extracted.
@param condition A criterion, which is applied for data to be extracted.
@returns A ``List`` of requested values.";

Begin@"`Private`";

$conn = Null;

connect[name_String] :=
   Module[{file},
      If[MatchQ[$conn, _DatabaseLink`SQLConnection],
         DatabaseLink`CloseSQLConnection@$conn];
      If[FileExistsQ@name,
         file = AbsoluteFileName@name;,
         Message[connect::name, name];
         Return@$Failed;];
   $conn = DatabaseLink`OpenSQLConnection@DatabaseLink`JDBC["SQLite", file];];
connect::name = "File `1` does not exist.";

get[combinations:{__}, condition:_:True] :=
   Module[{data, columns, replace, extractor},
      columns = DeleteDuplicates@Cases[combinations, _String, Infinity];
      With[{wrapped = condition/. s_String:> DatabaseLink`SQLColumn@s},
         data = DatabaseLink`SQLSelect[$conn, "data", columns, wrapped];];
      replace = MapIndexed[Function[{str, num}, str -> Slot@@num], columns];
      extractor = Function[Evaluate[combinations/. replace]];
      extractor@@ #&/@ data];

End[];
Block[{$ContextPath}, EndPackage[];];
