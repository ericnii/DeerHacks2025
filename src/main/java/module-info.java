module com.example.deerhacks2025 {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.deerhacks2025 to javafx.fxml;
    exports com.example.deerhacks2025;
}