# Programming assignment 3 (pa03) -- Practical end-to-end user cryptography

1. Create ssh key and set it up to log into gitlab/git-classes, take screenshots of it functioning.
Read the following links in full:
    * https://git-classes.mst.edu/help/ssh/README#generating-a-new-ssh-key-pair
    * https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process
    * https://help.github.com/articles/connecting-to-github-with-ssh/ (and sub-pages)

    Deliverable: `ssh-key.png` which should contain an image of the browser interface with your public key, and a terminal where you did an operation like git pull, with no need for a password.


2. Fully validate the Debian iso your downloaded for pa00, from within Debian.
Take screenshots of hash and signature verification steps.
    * https://www.debian.org/CD/faq/index.en.html#verify
    * https://www.debian.org/CD/verify

    Other related resources:
    * https://docs.kali.org/introduction/download-official-kali-linux-images
    * https://www.kali.org/downloads/
    * https://en.opensuse.org/SDB:Download_help#Checksums
    * https://tutorials.ubuntu.com/tutorial/tutorial-how-to-verify-ubuntu#0

    Deliverable: `iso-verify.png` where you show the commands and results to verify the hash against the dev pgp key, and the iso against the hash.


3. Set up email encryption using gnupg.

    1. Read the content at all of the links here: 
    https://mst-cs.gitlab.io/index_files/ContactPublicKey.html

    2. Create a gpg2 key with 4096 bit RSA and your campus email. 
    
    3. Set up your email a in mail client (optional), see the following for supported clients: https://en.wikipedia.org/wiki/GNU_Privacy_Guard#Application_support
    (KMail, Thunderbird, Claws-mail are nice, or Mutt if you dare try the Vim of email clients) or use webmail to keep it easy with https://www.mailvelope.com/en/
    
    4. Exchange and sign keys with 5 students in 3600 (either in person, or using a keyserver like https://keys.mailvelope.com/ with any client you choose).
    
    5. Encrypt separate back-and-forth discussions with 5 different students in 3600;
    take a single screenshot for each back-and-forth exchange.
    
    6. Get those same 5 students to sign your gpg2 public key at the command line in Debian;
    include your 5x signed key in your repo, and optionally (above) on the mailvelope or other keyserver.
    
    7. Send a single signed message encrypted to both me and and our TA/grader (Jeff Gould <jg7f9@mst.edu>) whose key is also on the syllabus, 
    with your 5x-peer-signed and ASCII-armored public key attached to the email.
    The subjet line should exactly read: "3600 pa03 gnupg email"

    Deliverables: `gpg2_conversation1.png`, `gpg2_conversation2.png`, `gpg2_conversation3.png`, `gpg2_conversation4.png`, `gpg2_conversation5.png`, `username_key.asc` where the png files show evidence of your encrypted signed conversations, and the asc file is your public key, with all signatures embedded in it.


4. With 5 students in the class (can be different or the same as for previous part), exchange back-and-forth communications in an open-source end-to-end PFS app of your choosing.
    
    1. Read: https://en.wikipedia.org/wiki/Forward_secrecy and https://en.wikipedia.org/wiki/Deniable_authentication first, then choose an app:
        * https://wire.com/ (particularly nice, centralized)
        * https://tox.chat/ (very cool tech, fully p2p)
        * https://ring.cx/ (very cool tech, fully p2p)
        * https://www.signal.org/
        * https://silence.im/
        * OTR (many clients on Jabber/XMPP, IRC, etc) or OMEMO. Both are open federated protocol with multiple applications
            * https://en.wikipedia.org/wiki/Off-the-Record_Messaging
            * https://en.wikipedia.org/wiki/OMEMO
            * https://conversations.im/ (particularly nice)
            * https://gajim.org/
            * https://chatsecure.org/
        * Retroshare signed messenging capabilities http://retroshare.net/ (also fully p2p, very flexible)
        * https://ricochet.im/ (tor-based, fully p2p)
        * http://goldbug.sourceforge.net/
    
        If you are aware of any others, please feel free to check with me to see if they meet the criteria.
        These are really the main contenders when it comes to open-source perfect-forward-secure text-based communications.
    
    2. Include screenshots in the repository of 5 exchanges. 

    Deliverables: `pfs_conversation1.png`, `pfs_conversation2.png`, `pfs_conversation3.png`, `pfs_conversation4.png`, `pfs_conversation5.png` which show evidence of 5 class conversations.

