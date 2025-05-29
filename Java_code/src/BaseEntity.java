//package Table;



// Lớp trừu tượng cơ sở cho tất cả các thực thể database
public abstract class BaseEntity {
    private String tableName;

    public String getTableName() {
        return this.tableName;
    }
}