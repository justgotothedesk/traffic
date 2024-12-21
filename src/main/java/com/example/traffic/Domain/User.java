package com.example.traffic.Domain;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.util.Date;
import java.util.List;

@Getter
@Setter
@ToString
@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long uid;
    private String name;
    private String id;
    private String password;
    private String nickname;

    @Temporal(TemporalType.TIMESTAMP)
    private Date createdDate;

    @OneToMany(mappedBy = "user_id", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<UserEvent> userEvent;

    @OneToMany(mappedBy = "user_id", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<PurchaseEvent> purchaseEvent;

    @OneToMany(mappedBy = "user_id", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Product> product;
}
