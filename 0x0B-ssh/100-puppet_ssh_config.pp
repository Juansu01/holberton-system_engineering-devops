# This puppet file configures a server

file_line { "PasswordAuthentication":
            path  => "/etc/ssh/ssh_config",
            line  => "    PasswordAuthentication no",
            match => "^    PasswordAuthentication",
            replace => true
        }

file_line { "IdentityFile":
            path  => "/etc/ssh/ssh_config",
            line  => "    IdentityFile ~/.ssh/holberton",
            match => "^    IdentityFile",
            replace => true
        }

