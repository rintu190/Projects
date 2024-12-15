package com.aurora.user_service.dtos;

public class UserDetailsDTO {
    private String id;
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    private String name;
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    private String age;

    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public UserDetailsDTO(String id,String name,String age){
        this.id = id;
        this.name = name;
        this.age = age;
    }

    

}
