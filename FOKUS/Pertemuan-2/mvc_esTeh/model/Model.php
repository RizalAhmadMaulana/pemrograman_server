<?php
    include_once("model/Book.php");

    class Model {
        public function getBooklist(){
            return array (
                "Jungle Book" => new Book("Junggle Book", "R.Kipling", "A classic book."),
                "Moonwalker" => new Book("Moonwalker", "J.Walker", ""),
                "PHP for Dummies" => new Book("PHP for Dummies", "Some Smart Guy", "")
            );
        }

        public function getBook($title){
            $allBooks = $this->getBooklist();
            return $allBooks[$title];
        }
    }
?>