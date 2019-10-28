CREATE SCHEMA CAA;
USE CAAcanvas;
SET SQL_SAFE_UPDATES = 0;

CREATE TABLE IF NOT EXISTS canvas(
     nomCanvas VARCHAR(43) NOT NULL,
     root VARCHAR(43) NOT NULL,
     borderwidth INTEGER DEFAULT 2,
     background VARCHAR(43) DEFAULT '#E4E4E4',
     height INTEGER NOT NULL,
     highlightbackground VARCHAR(43) DEFAULT 'none',
     highlightcolor VARCHAR(43) DEFAULT 'none',
     highlightthickness INTEGER DEFAULT 1,
     relief VARCHAR(43) DEFAULT 'flat',
     width INTEGER NOT NULL,
     x INTEGER DEFAULT 0,
     y INTEGER DEFAULT 0
);


CREATE TABLE IF NOT EXISTS button(
    nomButton VARCHAR(43) NOT NULL,
    root VARCHAR(43) NOT NULL,
    text TEXT DEFAULT '',
    textvariable VARCHAR(43) DEFAULT 'None',
    relief VARCHAR(43) DEFAULT 'flat',
    bg VARCHAR(43) DEFAULT '#AAAAAA',
    fg VARCHAR(43) DEFAULT '#000000',
    font VARCHAR(43) DEFAULT 'myFont',
    image VARCHAR(43) DEFAULT 'None',
    borderwidth INTEGER DEFAULT 2,
    x INTEGER DEFAULT 0,
     y INTEGER DEFAULT 0,
    width INTEGER NOT NULL,
    height INTEGER NOT NULL,
    command VARCHAR(43) DEFAULT 'None'
    );
    
    CREATE TABLE IF NOT EXISTS label(
    nomLabel VARCHAR(43) NOT NULL,
    root VARCHAR(43) NOT NULL,
    text TEXT DEFAULT '',
    textvariable VARCHAR(43) DEFAULT 'None',
    bg VARCHAR(43) DEFAULT '#AAAAAA',
    font VARCHAR(43) DEFAULT 'myFont',
    x INTEGER DEFAULT 0,
    y INTEGER DEFAULT 0,
    width INTEGER NOT NULL,
    height INTEGER NOT NULL
    );
    

INSERT INTO canvas (nomCanvas, root, height, width) VALUES ('test', 'root', 175, 176);

INSERT INTO button (nomButton, root, height, width) VALUES ('test', 'root', 175, 176);