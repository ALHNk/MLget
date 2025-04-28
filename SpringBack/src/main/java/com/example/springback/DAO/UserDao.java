package com.example.springback.DAO;

import com.example.springback.Entities.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface UserDao extends JpaRepository<User, Integer> {
    public void getUserByEmail(String email);
    public Optional<User> findByEmail(String email);
}
