```mermaid

classDiagram
direction LR
    class User {
	+UUID4 ID
        +String firstName
        +String lastName
        +String email
        +String password
        +Boolean isAdmin
        +register()
        +updateProfile()
        +delete()
    }
    class Place {
	+UUID4 ID
        +String title
        +String description
        +Float price
        +Float latitude
        +Float longitude
        +create()
        +update()
        +delete()
        +list()
    }
    class Review {
	+UUID4 ID
        +Int rating
        +String comment
        +create()
        +update()
        +delete()
        +listByPlace()
    }
    class Amenity {
	+UUID4 ID
        +String name
        +String description
        +create()
        +update()
        +delete()
        +list()
    }
    User "1" -- "*" Place : owns
    User "1" -- "*" Review : writes
    Place "1" -- "*" Review : receives
    Place "*" -- "*" Amenity : has

	style User fill:#424242,stroke:#E3100C,color:#E3100C
	style Place fill:#424242,stroke:#E3100C,color:#E3100C
	style Review fill:#424242,stroke:#E3100C,color:#E3100C
	style Amenity fill:#424242,stroke:#E3100C,color:#E3100C
