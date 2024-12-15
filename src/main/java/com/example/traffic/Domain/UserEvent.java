package com.example.traffic.Domain;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Getter
@Setter
public class UserEvent {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long uid;
    private Long timestamp;
    private String action;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", referencedColumnName = "uid", nullable = false, updatable = false)
    private User user;
}
