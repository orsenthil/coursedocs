Programming Environment Setup
=============================

Java
----

* `Download and Install Java 8`_

If you have multiple Java, then setting `JAVA_HOME` might be required.

::

    export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_111.jdk/Contents/Home


Submission
----------

::

    Execute the command: zip percolation.zip Percolation.java PercolationStats.java



Setup as per book site
----------------------

Install Java and install algs4 that is packaged and provided for the easy use.

1. http://algs4.cs.princeton.edu/mac/

::


    clear;echo -e "Launching algs4.app...

    Please type your OS X user password to begin the installation.
    Note: You won't see the characters as you type them.
    ";sudo bash '/Users/senthil/Downloads/algs4.app/Contents/Resources/launcher.sh' ${USER};exit &> /dev/null
    shannon-2:~ senthil$ bash
    bash: update_terminal_cwd: command not found
    bash: iterm2_preexec_invoke_cmd: command not found
    shannon-2:~ senthil$ clear;echo -e "Launching algs4.app...
    >
    > Please type your OS X user password to begin the installation.
    > Note: You won't see the characters as you type them.
    > ";sudo bash '/Users/senthil/Downloads/algs4.app/Contents/Resources/launcher.sh' ${USER};exit &> /dev/null






    Launching algs4.app...

    Please type your OS X user password to begin the installation.
    Note: You won't see the characters as you type them.

    Password:


















    ####################################################################
    #                                                                  #
    #            d8888 888      .d8888b.   .d8888b.        d8888       #
    #           d88888 888     d88P  Y88b d88P  Y88b      d8P888       #
    #          d88P888 888     888    888 Y88b.          d8P 888       #
    #         d88P 888 888     888         "Y888b.      d8P  888       #
    #        d88P  888 888     888  88888     "Y88b.   d88   888       #
    #       d88P   888 888     888    888       "888   8888888888      #
    #      d8888888888 888     Y88b  d88P Y88b  d88P         888       #
    #     d88P     888 88888888 "Y8888P88  "Y8888P"          888       #
    #                                                                  #
    ####################################################################
    #                                                                  #
    # Java Programming Environment Setup                               #
    # for Mac OS X - v4.0                                              #
    # Written by Hayk Martirosyan and Kevin Wayne                      #
    # Princeton University                                             #
    #                                                                  #
    ####################################################################

    Initializing functions and beginning installation...

    Creating installation directory at
    /usr/local/algs4

    #### Step 1 - Java #################################################

    % javac -version
    javac 1.8.0_111

    % java -version
    java version "1.8.0_111"
    Java(TM) SE Runtime Environment (build 1.8.0_111-b14)
    Java HotSpot(TM) 64-Bit Server VM (build 25.111-b14, mixed mode)

    Java 8 appears to be properly installed.

    Downloading java execution script from
    http://algs4.cs.princeton.edu/mac/java-algs4
    to
    /usr/local/bin/java-algs4

    Granting executable permission to
    /usr/local/bin/java-algs4

    Downloading javac execution script from
    http://algs4.cs.princeton.edu/mac/javac-algs4
    to
    /usr/local/bin/javac-algs4

    Granting executable permission to
    /usr/local/bin/javac-algs4

    Downloading java-cos226 execution script from
    http://algs4.cs.princeton.edu/mac/java-cos226
    to
    /usr/local/bin/java-cos226

    Granting executable permission to
    /usr/local/bin/java-cos226

    Downloading javac-cos226 execution script from
    http://algs4.cs.princeton.edu/mac/javac-cos226
    to
    /usr/local/bin/javac-cos226

    Granting executable permission to
    /usr/local/bin/javac-cos226

    #### Step 2 - Textbook Libraries ##################################

    Downloading algs4.jar from
    http://algs4.cs.princeton.edu/code/algs4.jar
    to
    /usr/local/algs4/algs4.jar

    #### Step 3 - Checkstyle ##########################################

    Downloading checkstyle from
    http://algs4.cs.princeton.edu/mac/checkstyle.zip
    to
    /usr/local/algs4/checkstyle.zip

    Extracting zip archive in place at
    /usr/local/algs4/checkstyle.zip
    and deleting .zip file.

    Downloading checkstyle-algs4.xml configuration file from
    http://algs4.cs.princeton.edu/mac/checkstyle-algs4.xml
    to
    /usr/local/algs4/checkstyle-algs4.xml

    Downloading checkstyle-cos226.xml configuration file from
    http://algs4.cs.princeton.edu/mac/checkstyle-cos226.xml
    to
    /usr/local/algs4/checkstyle-cos226.xml

    Downloading checkstyle-suppressions.xml file from
    http://algs4.cs.princeton.edu/mac/checkstyle-suppressions.xml
    to
    /usr/local/algs4/checkstyle-suppressions.xml

    Downloading checkstyle-algs4 execution script from
    http://algs4.cs.princeton.edu/mac/checkstyle-algs4
    to
    /usr/local/bin/checkstyle-algs4

    Granting executable permission to
    /usr/local/bin/checkstyle-algs4

    Downloading checkstyle-cos226 execution script from
    http://algs4.cs.princeton.edu/mac/checkstyle-cos226
    to
    /usr/local/bin/checkstyle-cos226

    Granting executable permission to
    /usr/local/bin/checkstyle-cos226

    #### Step 4 - Findbugs ############################################

    Downloading findbugs from
    http://algs4.cs.princeton.edu/mac/findbugs.zip
    to
    /usr/local/algs4/findbugs.zip

    Extracting zip archive in place at
    /usr/local/algs4/findbugs.zip
    and deleting .zip file.

    Downloading findbugs.xml configuration file from
    http://algs4.cs.princeton.edu/mac/findbugs.xml
    to
    /usr/local/algs4/findbugs.xml

    Downloading findbugs-algs4 execution script from
    http://algs4.cs.princeton.edu/mac/findbugs-algs4
    to
    /usr/local/bin/findbugs-algs4

    Granting executable permission to
    /usr/local/bin/findbugs-algs4

    Downloading findbugs-cos226 execution script from
    http://algs4.cs.princeton.edu/mac/findbugs-cos226
    to
    /usr/local/bin/findbugs-cos226

    Granting executable permission to
    /usr/local/bin/findbugs-cos226

    #### Step 5 - DrJava ##############################################

    Downloading DrJava from
    http://algs4.cs.princeton.edu/mac/DrJava.zip
    to
    /Applications/DrJava.zip

    Extracting zip archive in place at
    /Applications/DrJava.zip
    to create
    /Applications/DrJava.app

    Downloading DrJava configuration file from
    http://algs4.cs.princeton.edu/mac/.drjava
    to
    /Users/senthil/.drjava

    Creating a shortcut to DrJava on the desktop...

    #### Step 6 - Terminal #############################################

    Creating a shortcut to Terminal on the desktop...

    #### Step 7 - Test it out! #########################################

    Downloading the test Java program...

    Installation complete! Compiling test program...
    Test program compiled. Running...

    If you saw the bullseye and textbook graphic, the installation
    was successful and you are ready to start programming in Java.
    Continue with the introductory tutorial on the booksite.

    NOTE: If there were any error messages during this setup, check the
    troubleshooting section on the website or ask for help.

    A log file of this installation is saved at
    /usr/local/algs4/log.txt

    You should now close this window.
    shannon-2:~ senthil$ cat /usr/local/algs4/log.txt
    ####################################################################
    #                                                                  #
    #            d8888 888      .d8888b.   .d8888b.        d8888       #
    #           d88888 888     d88P  Y88b d88P  Y88b      d8P888       #
    #          d88P888 888     888    888 Y88b.          d8P 888       #
    #         d88P 888 888     888         "Y888b.      d8P  888       #
    #        d88P  888 888     888  88888     "Y88b.   d88   888       #
    #       d88P   888 888     888    888       "888   8888888888      #
    #      d8888888888 888     Y88b  d88P Y88b  d88P         888       #
    #     d88P     888 88888888 "Y8888P88  "Y8888P"          888       #
    #                                                                  #
    ####################################################################
    #                                                                  #
    # Java Programming Environment Setup                               #
    # for Mac OS X - v4.0                                              #
    # Written by Hayk Martirosyan and Kevin Wayne                      #
    # Princeton University                                             #
    #                                                                  #
    ####################################################################

    Initializing functions and beginning installation...

    Creating installation directory at
    /usr/local/algs4

    #### Step 1 - Java #################################################

    % javac -version
    javac 1.8.0_111

    % java -version
    java version "1.8.0_111"
    Java(TM) SE Runtime Environment (build 1.8.0_111-b14)
    Java HotSpot(TM) 64-Bit Server VM (build 25.111-b14, mixed mode)

    Java 8 appears to be properly installed.

    Downloading java execution script from
    http://algs4.cs.princeton.edu/mac/java-algs4
    to
    /usr/local/bin/java-algs4

    Granting executable permission to
    /usr/local/bin/java-algs4

    Downloading javac execution script from
    http://algs4.cs.princeton.edu/mac/javac-algs4
    to
    /usr/local/bin/javac-algs4

    Granting executable permission to
    /usr/local/bin/javac-algs4

    Downloading java-cos226 execution script from
    http://algs4.cs.princeton.edu/mac/java-cos226
    to
    /usr/local/bin/java-cos226

    Granting executable permission to
    /usr/local/bin/java-cos226

    Downloading javac-cos226 execution script from
    http://algs4.cs.princeton.edu/mac/javac-cos226
    to
    /usr/local/bin/javac-cos226

    Granting executable permission to
    /usr/local/bin/javac-cos226

    #### Step 2 - Textbook Libraries ##################################

    Downloading algs4.jar from
    http://algs4.cs.princeton.edu/code/algs4.jar
    to
    /usr/local/algs4/algs4.jar

    #### Step 3 - Checkstyle ##########################################

    Downloading checkstyle from
    http://algs4.cs.princeton.edu/mac/checkstyle.zip
    to
    /usr/local/algs4/checkstyle.zip

    Extracting zip archive in place at
    /usr/local/algs4/checkstyle.zip
    and deleting .zip file.

    Downloading checkstyle-algs4.xml configuration file from
    http://algs4.cs.princeton.edu/mac/checkstyle-algs4.xml
    to
    /usr/local/algs4/checkstyle-algs4.xml

    Downloading checkstyle-cos226.xml configuration file from
    http://algs4.cs.princeton.edu/mac/checkstyle-cos226.xml
    to
    /usr/local/algs4/checkstyle-cos226.xml

    Downloading checkstyle-suppressions.xml file from
    http://algs4.cs.princeton.edu/mac/checkstyle-suppressions.xml
    to
    /usr/local/algs4/checkstyle-suppressions.xml

    Downloading checkstyle-algs4 execution script from
    http://algs4.cs.princeton.edu/mac/checkstyle-algs4
    to
    /usr/local/bin/checkstyle-algs4

    Granting executable permission to
    /usr/local/bin/checkstyle-algs4

    Downloading checkstyle-cos226 execution script from
    http://algs4.cs.princeton.edu/mac/checkstyle-cos226
    to
    /usr/local/bin/checkstyle-cos226

    Granting executable permission to
    /usr/local/bin/checkstyle-cos226

    #### Step 4 - Findbugs ############################################

    Downloading findbugs from
    http://algs4.cs.princeton.edu/mac/findbugs.zip
    to
    /usr/local/algs4/findbugs.zip

    Extracting zip archive in place at
    /usr/local/algs4/findbugs.zip
    and deleting .zip file.

    Downloading findbugs.xml configuration file from
    http://algs4.cs.princeton.edu/mac/findbugs.xml
    to
    /usr/local/algs4/findbugs.xml

    Downloading findbugs-algs4 execution script from
    http://algs4.cs.princeton.edu/mac/findbugs-algs4
    to
    /usr/local/bin/findbugs-algs4

    Granting executable permission to
    /usr/local/bin/findbugs-algs4

    Downloading findbugs-cos226 execution script from
    http://algs4.cs.princeton.edu/mac/findbugs-cos226
    to
    /usr/local/bin/findbugs-cos226

    Granting executable permission to
    /usr/local/bin/findbugs-cos226

    #### Step 5 - DrJava ##############################################

    Downloading DrJava from
    http://algs4.cs.princeton.edu/mac/DrJava.zip
    to
    /Applications/DrJava.zip

    Extracting zip archive in place at
    /Applications/DrJava.zip
    to create
    /Applications/DrJava.app

    Downloading DrJava configuration file from
    http://algs4.cs.princeton.edu/mac/.drjava
    to
    /Users/senthil/.drjava

    Creating a shortcut to DrJava on the desktop...

    #### Step 6 - Terminal #############################################

    Creating a shortcut to Terminal on the desktop...

    #### Step 7 - Test it out! #########################################

    Downloading the test Java program...

    Installation complete! Compiling test program...
    Test program compiled. Running...

    If you saw the bullseye and textbook graphic, the installation
    was successful and you are ready to start programming in Java.
    Continue with the introductory tutorial on the booksite.

    NOTE: If there were any error messages during this setup, check the
    troubleshooting section on the website or ask for help.

    A log file of this installation is saved at
    /usr/local/algs4/log.txt

    You should now close this window.


.. _Download and Install Java 8: http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
