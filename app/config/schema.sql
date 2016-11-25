-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 28-12-2015 a las 12:16:13
-- Versión del servidor: 5.5.46-0ubuntu0.14.04.2
-- Versión de PHP: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_menu`
--

CREATE TABLE IF NOT EXISTS `tb_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `icono_html` varchar(40) DEFAULT 'fa-angle-double-right',
  `titulo` varchar(60) NOT NULL,
  `ruta_controlador` varchar(60) NOT NULL,
  `id_padre` int(11) NOT NULL DEFAULT '1',
  `descripcion` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_menu_menu_padre` (`id_padre`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=53 ;

--
-- Volcado de datos para la tabla `tb_menu`
--

INSERT INTO `tb_menu` (`id`, `icono_html`, `titulo`, `ruta_controlador`, `id_padre`, `descripcion`) VALUES
(1, 'fa-angle-double-right', 'NA', '#', 1, ''),
(2, 'fa-wifi', 'Accesos', 'accesos/', 1, 'Descripción de Accesos'),
(8, 'fa-angle-double-right', 'Gestión del Menú', 'accesos/menu', 2, ''),
(14, 'fa-list', 'Maestros', 'maestros/', 1, ''),
(23, 'fa-angle-double-right', 'Ubicaciones del Perú', 'maestros/departamento', 14, ''),
(26, 'fa-briefcase', 'Administración', 'administracion/', 1, ''),
(27, 'fa-angle-double-right', 'Gestión de Razones Sociales', 'administracion/razones_sociales', 26, ''),
(36, 'fa-child', 'Vacaciones', 'renta/', 1, ''),
(43, 'fa-angle-double-right', 'Gestión de Personal', 'administracion/personal', 26, ''),
(44, 'fa-angle-double-right', 'Gestión de Áreas', 'administracion/area', 26, ''),
(46, 'fa-angle-double-right', 'Gestión de Periodos', 'administracion/periodo', 26, ''),
(49, 'fa-angle-double-right', 'Gestión de Papeletas', 'vacaciones/papeleta', 36, ''),
(50, 'fa-angle-double-right', 'Gestión de Usuarios ', 'accesos/usuario', 2, ''),
(51, 'fa-angle-double-right', 'Gestión de Roles', 'accesos/rol', 2, ''),
(52, 'fa-angle-double-right', 'Gestión de Permisos', 'accesos/permiso', 2, '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_menu_usuario`
--

CREATE TABLE IF NOT EXISTS `tb_menu_usuario` (
  `id_menu` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `valor` tinyint(4) NOT NULL,
  PRIMARY KEY (`id_menu`,`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_menu_web`
--

CREATE TABLE IF NOT EXISTS `tb_menu_web` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(60) NOT NULL,
  `ruta_controlador` varchar(60) NOT NULL,
  `id_padre` int(11) NOT NULL DEFAULT '1',
  `id_upload` int(11) DEFAULT NULL,
  `descripcion` text NOT NULL,
  `icono_html` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_menu_menu_padre` (`id_padre`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Volcado de datos para la tabla `tb_menu_web`
--

INSERT INTO `tb_menu_web` (`id`, `titulo`, `ruta_controlador`, `id_padre`, `id_upload`, `descripcion`, `icono_html`) VALUES
(1, 'NA', '#', 1, NULL, '', '0'),
(2, 'Inicio', ' ', 1, NULL, '', 'home'),
(3, 'Nosotros', 'nosotros', 1, NULL, '', 'group'),
(4, 'Servicios', 'servicios', 1, NULL, '', 'newspaper-o'),
(5, 'Requisitos', 'requisitos', 1, NULL, '', 'list-ol'),
(6, 'Nuestra Flota', 'flota', 1, NULL, '', 'car'),
(7, 'Contacto', 'contacto', 1, NULL, '', 'location-arrow');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_permisos`
--

CREATE TABLE IF NOT EXISTS `tb_permisos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `llave` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Volcado de datos para la tabla `tb_permisos`
--

INSERT INTO `tb_permisos` (`id`, `nombre`, `llave`) VALUES
(1, 'Tareas de Administrador', 'admin_access'),
(4, 'Administrador RRHH', 'admin_rrhh'),
(6, 'Jefe de Área', 'jefe_area');


--
-- Estructura de tabla para la tabla `tb_roles`
--

CREATE TABLE IF NOT EXISTS `tb_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Volcado de datos para la tabla `tb_roles`
--

INSERT INTO `tb_roles` (`id`, `nombre`) VALUES
(1, 'SuperAdministrador'),
(2, 'Jefe de Área'),
(5, 'Administrador de Recursos Humanos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_roles_permisos`
--

CREATE TABLE IF NOT EXISTS `tb_roles_permisos` (
  `id_rol` int(11) NOT NULL,
  `id_permiso` int(11) NOT NULL,
  `valor` int(11) NOT NULL,
  PRIMARY KEY (`id_rol`,`id_permiso`) USING BTREE,
  KEY `fk_id_permiso_tb_permisos` (`id_permiso`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tb_roles_permisos`
--

INSERT INTO `tb_roles_permisos` (`id_rol`, `id_permiso`, `valor`) VALUES
(1, 1, 1),
(2, 6, 1),
(5, 1, 1),
(5, 4, 1),
(5, 6, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_usuario`
--

CREATE TABLE IF NOT EXISTS `tb_usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(40) NOT NULL,
  `contrasena` varchar(100) NOT NULL,
  `codigo_activacion` varchar(45) DEFAULT NULL,
  `id_usuario_estado` int(11) NOT NULL,
  `id_tabla` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `new_fk_suario_uusuario_estado` (`id_usuario_estado`),
  KEY `id_vw_tabla` (`id_tabla`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcado de datos para la tabla `tb_usuario`
--

INSERT INTO `tb_usuario` (`id`, `usuario`, `contrasena`, `codigo_activacion`, `id_usuario_estado`, `id_tabla`) VALUES
(1, 'admin', 'QJOPfBjSrktR5f4aZKOaGpdZs8fnwzYAoT3F2dOrIks=', '', 1, NULL),
(2, 'na', 'ladfkajdklfad', NULL, 3, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_usuario_correlativos`
--

CREATE TABLE IF NOT EXISTS `tb_usuario_correlativos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `valor` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=42 ;

--
-- Volcado de datos para la tabla `tb_usuario_correlativos`
--

INSERT INTO `tb_usuario_correlativos` (`id`, `valor`) VALUES
(1, 0),
(2, 0),
(3, 0),
(4, 0),
(5, 0),
(6, 0),
(7, 0),
(8, 0),
(9, 0),
(10, 0),
(11, 0),
(12, 0),
(13, 0),
(14, 0),
(15, 0),
(16, 0),
(17, 0),
(18, 0),
(19, 0),
(20, 0),
(21, 0),
(22, 0),
(23, 0),
(24, 0),
(25, 0),
(26, 0),
(27, 0),
(28, 0),
(29, 0),
(30, 0),
(31, 0),
(32, 0),
(33, 0),
(34, 0),
(35, 0),
(36, 0),
(37, 0),
(38, 0),
(39, 0),
(40, 0),
(41, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_usuario_estado`
--

CREATE TABLE IF NOT EXISTS `tb_usuario_estado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Volcado de datos para la tabla `tb_usuario_estado`
--

INSERT INTO `tb_usuario_estado` (`id`, `nombre`) VALUES
(1, 'Activo'),
(2, 'Activación Pendiente'),
(3, 'Suspendido'),
(4, 'Eliminado'),
(5, 'No Creado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_usuario_menus`
--

CREATE TABLE IF NOT EXISTS `tb_usuario_menus` (
  `id_usuaio` int(11) DEFAULT NULL,
  `id_menu` int(11) DEFAULT NULL,
  `valor` tinyint(4) DEFAULT NULL,
  KEY `id_usuaio` (`id_usuaio`,`id_menu`),
  KEY `id_menu` (`id_menu`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_usuario_permisos`
--

CREATE TABLE IF NOT EXISTS `tb_usuario_permisos` (
  `id_usuario` int(11) NOT NULL,
  `id_permisos` int(11) NOT NULL,
  `valor` tinyint(4) NOT NULL,
  PRIMARY KEY (`id_usuario`,`id_permisos`),
  KEY `fk_id_pmiso_tbbb_permisos_tb_` (`id_permisos`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tb_usuario_permisos`
--

INSERT INTO `tb_usuario_permisos` (`id_usuario`, `id_permisos`, `valor`) VALUES
(1, 1, 1),
(3, 4, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_usuario_roles`
--

CREATE TABLE IF NOT EXISTS `tb_usuario_roles` (
  `id_usuario` int(11) NOT NULL,
  `id_rol` int(11) NOT NULL,
  PRIMARY KEY (`id_usuario`,`id_rol`),
  KEY `fk_tb_roles_tb_usuario_roles` (`id_rol`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tb_usuario_roles`
--

INSERT INTO `tb_usuario_roles` (`id_usuario`, `id_rol`) VALUES
(1, 1);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tb_menu`
--
ALTER TABLE `tb_menu`
  ADD CONSTRAINT `tb_menu_ibfk_1` FOREIGN KEY (`id_padre`) REFERENCES `tb_menu` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tb_menu_web`
--
ALTER TABLE `tb_menu_web`
  ADD CONSTRAINT `tb_menu_web_ibfk_1` FOREIGN KEY (`id_padre`) REFERENCES `tb_menu_web` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tb_roles_permisos`
--
ALTER TABLE `tb_roles_permisos`
  ADD CONSTRAINT `tb_roles_permisos_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `tb_roles` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tb_roles_permisos_ibfk_2` FOREIGN KEY (`id_permiso`) REFERENCES `tb_permisos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tb_usuario_menus`
--
ALTER TABLE `tb_usuario_menus`
  ADD CONSTRAINT `tb_usuario_menus_ibfk_1` FOREIGN KEY (`id_usuaio`) REFERENCES `tb_usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tb_usuario_menus_ibfk_2` FOREIGN KEY (`id_menu`) REFERENCES `tb_menu` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tb_usuario_roles`
--
ALTER TABLE `tb_usuario_roles`
  ADD CONSTRAINT `tb_usuario_roles_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `tb_usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tb_usuario_roles_ibfk_2` FOREIGN KEY (`id_rol`) REFERENCES `tb_roles` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
