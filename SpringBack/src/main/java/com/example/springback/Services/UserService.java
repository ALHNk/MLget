package com.example.springback.Services;

import com.example.springback.DAO.UserDao;
import com.example.springback.DTO.UserDTO;
import com.example.springback.Entities.User;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.Map;

@Service
public class UserService {
    private final UserDao userDao;
    private final PasswordEncoder passwordEncoder;
    private final AuthenticationManager authenticationManager;
    private final JwtService jwtService;

    public UserService(UserDao userDao, PasswordEncoder passwordEncoder, AuthenticationManager authenticationManager, JwtService jwtService) {
        this.userDao = userDao;
        this.passwordEncoder = passwordEncoder;
        this.authenticationManager = authenticationManager;
        this.jwtService = jwtService;
    }

    public void save(UserDTO dto) {
        try{
            User user = new User();
            user.setEmail(dto.getEmail());
            user.setPassword(passwordEncoder.encode(dto.getPassword()));
            userDao.save(user);
        }
        catch(Exception e){
            throw new RuntimeException(e);
        }
    }

    public Map<String, String> loginUser(UserDTO request) {
        authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(
                        request.getEmail(),
                        request.getPassword()
                )
        );
        User user = userDao.findByEmail(request.getEmail()).orElseThrow(() -> new UsernameNotFoundException("User with email not found"));


        String accessToken = jwtService.generateToken(user);

        Map<String, String> tokens = new HashMap<>();
        tokens.put("access_token", accessToken);

        return tokens;
    }

}
