package com.example.springback.controllers;

import com.example.springback.Entities.Try;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("try")
public class TryController {
    @PostMapping("/")
    public String post(@RequestBody Try tr) {
        return "success " + tr.getName() + " " + tr.getSurname();
    }
    @GetMapping("/")
    public String get() {
        return "success";
    }
}
