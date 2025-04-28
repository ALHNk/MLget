package com.example.springback.controllers;

import com.example.springback.DTO.UserDTO;
import com.example.springback.Services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/auth")
public class UserController {
    private final UserService userService;

    @Autowired
    public UserController(UserService userService) {
        this.userService = userService;
    }

    @PostMapping("/register")
    public ResponseEntity<?> register(@RequestBody UserDTO dto) {
        try{
            userService.save(dto);
            return ResponseEntity.ok().contentType(MediaType.APPLICATION_JSON).body("User registered successfully");
        }
        catch(Exception e){
            return ResponseEntity.badRequest().contentType(MediaType.APPLICATION_JSON).body(e.getMessage());
        }
    }
    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody UserDTO request) {
        try {
            Map<String, String> tokens = userService.loginUser(request);
            return ResponseEntity.ok().contentType(MediaType.APPLICATION_JSON).body(tokens);
        }catch (Exception e){
            return ResponseEntity.badRequest().contentType(MediaType.APPLICATION_JSON).body(e.getMessage());
        }
    }
}
