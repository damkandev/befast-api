-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 15-07-2023 a las 23:24:05
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
-- Base de datos: `moltodeli`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE `categorias` (
  `categoriaid` int NOT NULL,
  `nombre` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `descripcion` varchar(200) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cocinas`
--

CREATE TABLE `cocinas` (
  `cocinaid` int NOT NULL,
  `userid` int NOT NULL,
  `pais` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `ciudad` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `categoria` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `empleados` int NOT NULL,
  `calle` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `nroCasa` int NOT NULL,
  `nombre` varchar(20) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cocinas_productos`
--

CREATE TABLE `cocinas_productos` (
  `productoid` int NOT NULL,
  `nombre` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `tipo` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `descripcion` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `cocinaid` int NOT NULL,
  `stock` int DEFAULT NULL,
  `imagen` varchar(40) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `categoriaid` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sitio_ecommerce`
--

CREATE TABLE `sitio_ecommerce` (
  `nombre_dominio` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `userid` int NOT NULL,
  `cocinaid` int NOT NULL,
  `nombre` varchar(30) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `userid` int NOT NULL COMMENT 'Identificador Primario de Usuario ',
  `nombre` varchar(30) COLLATE utf8mb4_general_ci NOT NULL COMMENT 'Nombre completo del usuario',
  `correo` varchar(30) COLLATE utf8mb4_general_ci NOT NULL COMMENT 'Correo Electronico del usuario',
  `contraseña` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `role` int DEFAULT '0',
  `payed` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='En esta tabla se almacenaran los usuarios de Moltodeli';

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`categoriaid`);

--
-- Indices de la tabla `cocinas`
--
ALTER TABLE `cocinas`
  ADD PRIMARY KEY (`cocinaid`),
  ADD KEY `cocinas_FK` (`userid`);

--
-- Indices de la tabla `cocinas_productos`
--
ALTER TABLE `cocinas_productos`
  ADD PRIMARY KEY (`productoid`),
  ADD KEY `cocinas_productos_FK` (`cocinaid`),
  ADD KEY `cocinas_productos_FK_1` (`categoriaid`);

--
-- Indices de la tabla `sitio_ecommerce`
--
ALTER TABLE `sitio_ecommerce`
  ADD PRIMARY KEY (`nombre_dominio`),
  ADD KEY `sitio_ecommerce_FK` (`userid`),
  ADD KEY `sitio_ecommerce_FK_1` (`cocinaid`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`userid`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categorias`
--
ALTER TABLE `categorias`
  MODIFY `categoriaid` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cocinas`
--
ALTER TABLE `cocinas`
  MODIFY `cocinaid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `cocinas_productos`
--
ALTER TABLE `cocinas_productos`
  MODIFY `productoid` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `userid` int NOT NULL AUTO_INCREMENT COMMENT 'Identificador Primario de Usuario ', AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cocinas`
--
ALTER TABLE `cocinas`
  ADD CONSTRAINT `cocinas_FK` FOREIGN KEY (`userid`) REFERENCES `usuarios` (`userid`);

--
-- Filtros para la tabla `cocinas_productos`
--
ALTER TABLE `cocinas_productos`
  ADD CONSTRAINT `cocinas_productos_FK` FOREIGN KEY (`cocinaid`) REFERENCES `cocinas` (`cocinaid`),
  ADD CONSTRAINT `cocinas_productos_FK_1` FOREIGN KEY (`categoriaid`) REFERENCES `categorias` (`categoriaid`);

--
-- Filtros para la tabla `sitio_ecommerce`
--
ALTER TABLE `sitio_ecommerce`
  ADD CONSTRAINT `sitio_ecommerce_FK` FOREIGN KEY (`userid`) REFERENCES `usuarios` (`userid`),
  ADD CONSTRAINT `sitio_ecommerce_FK_1` FOREIGN KEY (`cocinaid`) REFERENCES `cocinas` (`cocinaid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
