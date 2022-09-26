package recursion.bst;

public class main {

    static class Node {
        int data;
        Node left;
        Node right;

        int getData() {
            return data;
        }

        void setData(int data) {
            this.data = data;
        }

        public Node getLeft() {
            return left;
        }

        public void setLeft(Node left) {
            this.left = left;
        }

        public Node getRight() {
            return right;
        }

        public void setRight(Node right) {
            this.right = right;
        }
    }
}
