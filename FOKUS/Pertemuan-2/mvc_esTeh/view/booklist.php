<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table border="1">
        <tbody>
            <tr>
                <td>Title</td>
                <td>Author</td>
                <td>description</td>
            </tr>
        </tbody>
        <?php
            foreach ($books as $book) {
                echo '<tr><td><a href ="index.php?book=' . 
                    $book->title . '">' . $book->title . '</a></td><td>' . 
                    $book->author . '</td><td>' . $book->description . '</td><tr>';
            }
        ?>
    </table>
</body>
</html>