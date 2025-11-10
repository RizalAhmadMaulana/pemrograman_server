<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the website, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/
 *
 * @package WordPress
 */
define('WP_REDIS_HOST', 'redis');
define('WP_REDIS_PORT', 6379);
define('WP_CACHE', true);

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress_dp' );

/** Database username */
define( 'DB_USER', 'a71b' );

/** Database password */
define( 'DB_PASSWORD', 'a71b' );

/** Database hostname */
define( 'DB_HOST', 'mysql' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'ZWL!P?&~UiBNd h,+FG}AG/K;0{:f{+3_h TCGW@K&eyrgh:qF$GTqEUh(A@@1Lt' );
define( 'SECURE_AUTH_KEY',  '@4>IkDSuI}+fYFgWN(K@0|{a;<u!dY?5_Pr.KNp_fKm4XQFrLz(VKfCl@Fn]Wa3[' );
define( 'LOGGED_IN_KEY',    '0-`B> vXRHFU;.$W ~q]l@4p<><DO$UUsj]Y7L.fspheHE-(,/`j&f,]-u:WB IY' );
define( 'NONCE_KEY',        'xFPMtYMR-6MBr&<H(@T-zOKa5PmXv-+wk?|>)NlmnoPyg{n:`_e>b,nFj];S5G,M' );
define( 'AUTH_SALT',        'o|_R,J_%<4`H|X!}s+ sPvkY]5;R@}S%REn/.41Ttbf^+<S-%9A= OSgq(m&BP0x' );
define( 'SECURE_AUTH_SALT', 'nkb)l.pr+7>Fko HSlQ}UP/0WeLV;?(c#aXqF&O[|jTyOI`*lX>||JM7[ hEd)YR' );
define( 'LOGGED_IN_SALT',   'nXnErGFzJll^Le^FmtgKXdR3680(:`=e+e=-qOWP_`W1j$-uv)b|U4+mYRvw960z' );
define( 'NONCE_SALT',       '~?:BJu3?W{deET5}S6%cjl;t{D6b0<rU=gv(>~Z|Pf4j53dazq4ST7t7qAZGGdy<' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 *
 * At the installation time, database tables are created with the specified prefix.
 * Changing this value after WordPress is installed will make your site think
 * it has not been installed.
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/#table-prefix
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */

define('FS_METHOD', 'direct');

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
