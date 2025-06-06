package com.example.springback.Services;

import com.example.springback.DAO.UserDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

@Service
public class CustonUserDetailService implements UserDetailsService {
    @Autowired
    private UserDao userDao;



    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        return (UserDetails) userDao.findByEmail(username).orElseThrow(() -> new UsernameNotFoundException("User with email not found"));
    }
}
