-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th4 30, 2023 lúc 12:37 PM
-- Phiên bản máy phục vụ: 10.4.28-MariaDB
-- Phiên bản PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `downloadhistory`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `download_history`
--

CREATE TABLE `download_history` (
  `id` int(11) NOT NULL,
  `video_title` varchar(255) NOT NULL,
  `video_url` varchar(2083) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `download_history`
--

INSERT INTO `download_history` (`id`, `video_title`, `video_url`, `timestamp`) VALUES
(1, 'Khi Nào Mới Chịu Nói Yêu Em (Remix)', 'https://www.youtube.com/watch?v=GK8UzkjGIAg', '2023-04-30 10:07:36'),
(2, 'PHÚC DU - yêu anh đi mẹ anh bán bánh mì (MV OFFICIAL)', 'https://www.youtube.com/watch?v=-7sISWuTdj0', '2023-04-30 10:09:51'),
(3, 'DẬY MÀ ĐI', 'https://www.youtube.com/watch?v=rKkDicWd-KA', '2023-04-30 10:12:16');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `download_history`
--
ALTER TABLE `download_history`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `download_history`
--
ALTER TABLE `download_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
