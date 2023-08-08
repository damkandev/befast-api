-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 08-08-2023 a las 21:14:45
-- Versión del servidor: 8.0.30
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `befast`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `apoderado`
--

CREATE TABLE `apoderado` (
  `idapoderado` int NOT NULL,
  `nombres` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `apellido_p` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `apellido_m` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `telefono` int NOT NULL,
  `rut` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `apoderadosup`
--

CREATE TABLE `apoderadosup` (
  `idapoderadosup` int NOT NULL,
  `nombres` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `apellido_p` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `apellido_m` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `telefono` int NOT NULL,
  `rut` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `curso`
--

CREATE TABLE `curso` (
  `idcurso` int NOT NULL,
  `nivel` int NOT NULL,
  `letra` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante`
--

CREATE TABLE `estudiante` (
  `idestudiante` int NOT NULL,
  `idcurso` int DEFAULT NULL,
  `nombres` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `apellido_p` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `apellido_m` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `rut` int NOT NULL,
  `telefono` int NOT NULL,
  `direccion` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `idapoderado` int DEFAULT NULL,
  `idapoderadosup` int DEFAULT NULL,
  `avatar` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inspector`
--

CREATE TABLE `inspector` (
  `idinspector` int NOT NULL,
  `nombres` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `apellido_p` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `apellido_m` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `rut` int NOT NULL,
  `telefono` int NOT NULL,
  `direccion` varchar(60) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `userid` int NOT NULL COMMENT 'Identificador Primario de Usuario ',
  `nombre` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'Nombre completo del usuario',
  `correo` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'Correo Electronico del usuario',
  `contraseña` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `role` int DEFAULT '0',
  `payed` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='En esta tabla se almacenaran los usuarios de Moltodeli';

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`userid`, `nombre`, `correo`, `contraseña`, `role`, `payed`) VALUES
(4, 'damian', 'damian@befast.com', 'gAAAAABk0Xjv-csrHvF3T3-e0ZT28o6wem1wlIlDXESbDGzo5XDJpN5Vl1msYaTSVW5Hvf-zQpMs_xlfQ9Lo7eS36nWHOd6PxQ==', 0, 0),
(5, 'damian', 'damian@befast.com', 'gAAAAABk0Xj6sxs1vcm27iR9roQ1FBwevCRyJq4D36ba9AuAV-nrYs_gv1TvmBu9jmHr0sAvfa0Td3u-pvDKrVAcwc1aBS0uaA==', 0, 0),
(6, 'damian', 'damian@befast.com', 'gAAAAABk0XkOp1xiUCokmFhDYbLcYj2bTNhOPitL5sqVIoJFD_VB9YqYDuuJnmnFaYV8NLzNAuhexI_G3LSUVK7E0v0CWn6BuQ==', 0, 0),
(7, 'damian', 'damian@befast.com', 'gAAAAABk0XkzYtG5WykLjW6p3vvCOb6oiFELM5wPuDcItsLpfdK1UDwwiBEMS93e6xZC8PdAMyMgyF3FQikJ2sRJZ7LwKQIM0Q==', 0, 0),
(8, 'damian', 'damian@befast.com', 'gAAAAABk0Xk4uJx2gRs6GIhumnHLBDFsGwGf-8HIMj8Kd2tYoBgxn8rJNFldM163XmEZ1PZ-ppGOPt-4id1i_h8_kisHtyInNw==', 0, 0),
(9, 'damian', 'damian@befast.com', 'gAAAAABk0XlybVlKdL9HqAf7cfKcz0woH0OKld_f6RDyYJ1gB9IrtsW4HGkIsNZrmNCKeaLmDraOk5tL-Ysr44XYTU7QDh0_bg==', 0, 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `apoderado`
--
ALTER TABLE `apoderado`
  ADD PRIMARY KEY (`idapoderado`);

--
-- Indices de la tabla `apoderadosup`
--
ALTER TABLE `apoderadosup`
  ADD PRIMARY KEY (`idapoderadosup`);

--
-- Indices de la tabla `curso`
--
ALTER TABLE `curso`
  ADD PRIMARY KEY (`idcurso`);

--
-- Indices de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`idestudiante`),
  ADD KEY `estudiante_FK` (`idcurso`),
  ADD KEY `estudiante_FK_1` (`idapoderado`),
  ADD KEY `estudiante_FK_2` (`idapoderadosup`);

--
-- Indices de la tabla `inspector`
--
ALTER TABLE `inspector`
  ADD PRIMARY KEY (`idinspector`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`userid`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `apoderado`
--
ALTER TABLE `apoderado`
  MODIFY `idapoderado` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `apoderadosup`
--
ALTER TABLE `apoderadosup`
  MODIFY `idapoderadosup` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `curso`
--
ALTER TABLE `curso`
  MODIFY `idcurso` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  MODIFY `idestudiante` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `inspector`
--
ALTER TABLE `inspector`
  MODIFY `idinspector` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `userid` int NOT NULL AUTO_INCREMENT COMMENT 'Identificador Primario de Usuario ', AUTO_INCREMENT=10;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD CONSTRAINT `estudiante_FK` FOREIGN KEY (`idcurso`) REFERENCES `curso` (`idcurso`),
  ADD CONSTRAINT `estudiante_FK_1` FOREIGN KEY (`idapoderado`) REFERENCES `apoderado` (`idapoderado`),
  ADD CONSTRAINT `estudiante_FK_2` FOREIGN KEY (`idapoderadosup`) REFERENCES `apoderadosup` (`idapoderadosup`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
