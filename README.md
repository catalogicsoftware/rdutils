
# rdutils

This repo contains miscellaneous scripts that are very handy in day to
day work.

## stacktrace.py

A script to remove clutter from huge stack traces. It does this by
keeping only lines that contain classes with a given prefix. For
example, if our classes are in the package `com.example`, a sample
output from the script might looks like this:

    $ cat logfile.txt | stacktrace.py 
    
    com.example.AuthorizationException: null
    	at com.example.UserHelperImpl.deleteUser(UserHelperImpl.java:95)
    	at com.example.UserController.deleteUser(UserController.java:316)
            ...
    	at com.example.LicenseFilter.doFilter(LicenseFilter.java:42)
            ...
    	at com.example.SecurityFilter.doFilter(SecurityFilter.java:224)
            ...

In addition to this, the script also keeps at least one line for each
exception in the chain. Here is a sample:

    $ cat logfile.txt | stacktrace.py 
    
    Context initialization failed org.springframework.beans.factory.CannotLoadBeanClassException: Error loading class [com.example.ResourceHandler] for bean with name 'testResourceHandler' defined in ServletContext resource [/WEB-INF/applicationContext.xml]: problem with class file or dependent class; nested exception is java.lang.NoClassDefFoundError: com.example.ResourceHandler not found from bundle [com.example.test (com.example.test)]
    	at org.springframework.beans.factory.support.AbstractBeanFactory.resolveBeanClass(AbstractBeanFactory.java:1272)
            ...
    Caused by: java.lang.NoClassDefFoundError: com.example.ResourceHandler not found from bundle [com.example.test (com.example.test)]
    	at org.eclipse.gemini.blueprint.util.BundleDelegatingClassLoader.findClass(BundleDelegatingClassLoader.java:110)
            ...
    	... 32 common frames omitted
    Caused by: org.eclipse.virgo.kernel.osgi.framework.ExtendedNoClassDefFoundError: com/example/ResourceHandler in KernelBundleClassLoader: [bundle=com.example.test_2.4.0.201605061424] in KernelBundleClassLoader: [bundle=com.example.test_2.4.0.201605061424]
    	at org.eclipse.virgo.kernel.userregion.internal.equinox.KernelBundleClassLoader.loadClass(KernelBundleClassLoader.java:152)
            ...
    	... 38 common frames omitted
    Caused by: org.eclipse.virgo.kernel.osgi.framework.ExtendedNoClassDefFoundError: com/example/ResourceHandler in KernelBundleClassLoader: [bundle=com.example.test_2.4.0.201605061424]
    	at org.eclipse.virgo.kernel.userregion.internal.equinox.KernelBundleClassLoader.defineClass(KernelBundleClassLoader.java:255)
            ...
    	... 43 common frames omitted
    Caused by: java.lang.NoClassDefFoundError: com/example/ResourceHandler
    	at java.lang.ClassLoader.defineClass1(Native Method)
            ...
    	... 55 common frames omitted
    Caused by: org.eclipse.virgo.kernel.osgi.framework.ExtendedClassNotFoundException: com.example.ResourceHandler in KernelBundleClassLoader: [bundle=com.example.test_2.4.0.201605061424]
    	at org.eclipse.virgo.kernel.userregion.internal.equinox.KernelBundleClassLoader.loadClass(KernelBundleClassLoader.java:150)
            ...
    	... 59 common frames omitted
    Caused by: java.lang.ClassNotFoundException: com.example.ResourceHandler
    	at org.eclipse.osgi.internal.loader.BundleLoader.findClassInternal(BundleLoader.java:455)
            ...
    	... 60 common frames omitted

The script works with python 2.x but it would be trivial to make it
work with python 3.x. 

By default, the script looks for classes in `com.example` package. To
change this to your own package, change the value of the variable
`OUR_PKG` in the script.  



