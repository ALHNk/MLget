package com.example.springback.DTO;

import lombok.Data;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Size;

@Data
public class UserDTO {
    @NotBlank(message = "email must be valid")
    private String email;
    @NotBlank(message = "password must be valid")
    @Size(min = 6, message = "password must contain at least 6 characters")
    private String password;

}
