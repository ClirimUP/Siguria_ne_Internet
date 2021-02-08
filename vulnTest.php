&lt;?php


// Creating a database connection, because sql injection starts with a database :) , Please note this database must exist on your server.

$serverName = "localhost";
$userName = "root";
$password = "********";
$databaseName = "socialnetwork";


// this argument will be passed from our python script

$userFromArg = $_POST['userid'];

$dbcn = new mysqli($serverName, $userName, $password,$databaseName);

if($dbcn-&gt;connect_error)
{
    die("Connection failed:". $dbcn-&gt;connect_error);
}



$sql = "SELECT userID, userName AS max FROM user where userID=$userFromArg";
    $result = $dbcn-&gt;query($sql);

    if ($result-&gt;num_rows &gt; 0) {
        $row = $result-&gt;fetch_assoc();
        $name = $row["userName"];
    echo $name;
    }else {
        echo $fail;
        exit();
    }


?&gt
