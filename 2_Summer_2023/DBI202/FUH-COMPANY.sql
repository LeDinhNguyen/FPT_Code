USE FUH_COMPANY

-- 1. HIEN THI TAT CA NHAN VIEN TRONG CONG TY
SELECT *
FROM tblEmployee

-- 2. HIEN THI 10 NHAN VIEN TRONG CONG TY
SELECT TOP 10 *
FROM tblEmployee

/*
3. HIEN THI THONG TIN TAT CA NHAN VIEN NHUNG CHI LAY THONG TIN 
"MA SO", "TEN", "DIA CHI", "NGAY BAT DAU DI LAM"
*/
SELECT empSSN, empName, empAddress, empStartdate
FROM tblEmployee

/*
4. HIEN THI THONG TIN NHAN VIEN TUONG UNG
empSSN --> Ma so NV
empName --> Ten NV
empAddress --> Dia chi
empStartDate --> Ngay bat dau lam viec
*/
SELECT empSSN AS 'Ma so NV', empName AS 'Ten NV', empAddress AS 'Dia chi', empStartdate AS 'Ngay bat dau lam viec'
FROM tblEmployee

/*
5. HIEN THI 5 NHAN VIEN DAU TIEN CAC THONG TIN empSSN, 
empName DOI THANH "TEN NV", empSex, empAddress 
*/
SELECT top 5 empSSN, empName AS 'Ten NV', empAddress AS 'Address', empSex
FROM tblEmployee

-- 6. LAY TAT CA CAC NHAN VIEN CO LUON > 30000
SELECT * 
FROM tblEmployee
WHERE empSalary > 30000

-- 7. LAY TAT CA CAC NHAN VIEN CO LUON > 30000 VA LA NU
SELECT * 
FROM tblEmployee
WHERE empSalary > 30000 AND empSex = 'F'

-- 8. LAY TAT CA CAC NHAN VIEN KHONG CO NGUOI QUAN LY (MAY THANG MO COI)
SELECT *
FROM tblEmployee
WHERE supervisorSSN IS NULL

-- 9. LAY TAT CA CAC NHAN VIEN CO CHU "Hoàng"
SELECT *
FROM tblEmployee
WHERE empName LIKE '%Hoàng%'

/*
10. HAY HIEN THI THONG TIN NHAN VIEN
BAO GOM mã số, họ tên, giới tính, lương và ngày làm việc
theo thứ tự lương tăng dần
*/
SELECT *
FROM tblEmployee
ORDER BY empSalary

/*
11. HAY LIET KE tên nhân viên, lương, 'ngày vào làm'
SAU ĐÓ SẮP XẾP GIẢM DẦN THEO 'ngày vào làm'
BIET RANG NHAN VIEN LÀ 'nữ'
*/
SELECT empName, empSalary, empStartdate
FROM tblEmployee
WHERE empSex = 'F'
ORDER BY empStartdate DESC

/*
12. HAY HIEN THI THONG TIN NHAN VIEN
BAO GOM 'mã số', 'họ tên', 'giới tính', 'lương' VA 'ngày làm việc'
THEO THU TU NGAY LAM VIEC DESC
*/
SELECT empSSN, empName, empSex, empSalary, empStartdate
FROM tblEmployee
ORDER BY empStartdate DESC

/*
13. HAY HIEN THI THONG TIN NHAN VIEN
BAO GOM 'mã số', 'họ tên', 'giới tính', 'lương' VA 'ngày làm việc'
'lương' TANG DAN
THEO THU TU 'ngày làm việc' DESC
*/
SELECT empSSN, empName, empSex, empSalary, empStartdate
FROM tblEmployee
ORDER BY empSalary ASC, empStartdate DESC

-- 14.
SELECT empSSN, empName, empSalary, empBirthdate, empAddress
FROM tblEmployee

--15 
SELECT *
FROM tblEmployee
WHERE supervisorSSN IS NULL AND empName LIKE N'Nguyễn%' AND empAddress = N'TP. Hồ Chí Minh'

--16
SELECT *
FROM tblEmployee
WHERE supervisorSSN IS NOT NULL AND empSalary > 10000 AND empAddress = N'TP. Hồ Chí Minh'

--17
SELECT *
FROM tblEmployee
WHERE supervisorSSN IS NOT NULL AND empSalary > 10000 AND empAddress = N'TP. Hồ Chí Minh'
ORDER BY empStartdate ASC, empSalary DESC

-- 18
SELECT empSSN, empName, empSex, empSalary, empStartdate
FROM tblEmployee
WHERE empSalary > 30000
ORDER BY empBirthdate DESC, empStartdate ASC

-- 19
SELECT *
FROM tblEmployee
WHERE empName like N'%Giang' and empSex = N'F'

-- 20
SELECT *
FROM tblEmployee
WHERE empName LIKE N'Vũ%' AND (empAddress = N'TP. Hồ Chí Minh' OR empAddress = N'TP. Hà Nội')

-- 21
SELECT *
FROM tblEmployee
WHERE empName LIKE N'%Hồng%' AND empName NOT LIKE N'%Hồng' AND empName NOT LIKE N'Hồng%'
-- Cách 2: WHERE empName LIKE N'%_Hồng 

-- PHẦN 2: CÁC HÀM PHỔ BIẾN VÀ TRUY VẤN NÂNG CAO
SELECT *
FROM tblEmployee
WHERE MONTH(empBirthdate) = 2

-- CÁC HÀM PHỔ BIẾN
--22 HIỂN THỊ THÔNG TIN NHÂN VIÊN VÀ THÁNG SINH
USE FUH_COMPANY
SELECT * 
FROM tblEmployee
WHERE MONTH(empBirthdate) = 2
--23 THÔNG TIN MÃ NHÂN VIÊN TÊN NV, THÁNG SINH
--24 tháng sinh lớn hơn 4
--25 theo thứ tự giảm dần
SELECT empSSN AS N'MÃ NHÂN VIÊN', empName AS N'TÊN NHÂN VIÊN', MONTH(empBirthdate) as N'Tháng sinh'
FROM tblEmployee
WHERE MONTH(empBirthdate) > 4
ORDER BY MONTH(empBirthdate) 


select empSSN as N'Ma nhan vien', empName as N'Ten nhan vien', MONTH(empBirthdate) as N'Thang sinh'
from tblEmployee
where month(empBirthdate) in (1,3,5,7,9)
order by month(empBirthdate) 

-- hiển thị thông tin nơi ở riêng biệt của nhân viên
select distinct empAddress
from tblEmployee
-- tính tuổi theo năm
select *
from tblEmployee
where year(getdate()) - year(empBirthdate) > 40
--tính tuổi theo ngày tháng năm
sElECt *
fRoM tblEmployee
wHeRE FLOOR((DATEDIFF(DAY,empBirthdate,getdate())/365.25)) > 40


-- tên của những nhân viên là quản lý của những nhân viên khác
sElEcT empName
frOm tblEmployee
where empSSN in (
  sElEct distinct supervisorSSN
  from tblEmployee
  where supervisorSSN is not null
)
select empName
from tblEmployee
where empSSN in (
 select distinct supervisorSSN
 from tblEmployee
)

--32 33 liệt kê ms, tên, giới tính, địa chỉ, của các nhân viên là các quản lý của phòng ban
select empSSN, empName, empSex, empAddress
from tblEmployee
where empSSN in (
 select distinct mgrSSN
 from tblDepartment
)
-- liệt kê những nhân viên có người thân
select *
FROM tblEmployee
WHERE empSSN in (
select distinct empSSN
from tblDependent
)
--NHÂN VIÊN CÓ THAM GIA LÀM DỰ ÁN
SELECT *
FROM tblEmployee
WHERE empSSN IN (
SELECT DISTINCT empSSN
FROM tblWorksOn
)
--ĐỊA ĐIỂM CÓ ĐẶT PHÒNG BAN
SELECT *
FROM tblLocation
WHERE locNum IN (
  SELECT DISTINCT depNum
  FROM tblDepLocation
)
--ĐỊA ĐIỂM CÓ
SELECT*
FROM tblDepartment
WHERE depNum IN (
  SELECT DISTINCT depNum
  FROM tblProject
)
--VỪA LÀ QUẢN LÝ PHÒNG BAN VỪA THAM GIA DỰ ÁN
SELECT *
FROM tblEmployee
where empSSN in (
 select distinct mgrSSN
 from tblDepartment
) AND empSSN IN (
  SELECT DISTINCT empSSN
  FROM tblWorksOn
)

-- NV CÓ THÂN NHÂN ĐANG LÀM QUẢN LÝ PHÒNG BAN
SELECT *
FROM tblDependent
WHERE empSSN IN(
  SELECT DISTINCT empSSN
  from tblEmployee
  where empSSN in (
    select distinct mgrSSN
    from tblDepartment
  )
 )
 --40 THÔNG TIN NHÂN VIÊN CÓ THÁNG SINH LÀ CHẴN
 SELECT *
 FROM tblEmployee
 WHERE MONTH(empBirthdate)%2 = 0
--41 HIẾN THỊ THÔNG TIN NHÂN VIÊN CÓ THÁNG SINH LÀ CHẴN SAU ĐÓ SẮP XẾP GIẢM DÂN THEO THÁNG SINH
 SELECT *
 FROM tblEmployee
 WHERE MONTH(empBirthdate)%2 = 0
 ORDER BY YEAR(empBirthdate) desc
 --42HAY4 HIỆN THỊ THÔNG TIN MÃ NHÂN VIÊN TÊN NHÂN VIÊN VÀ NGÀY SINH THÁNG SINH VÀ CÓ NĂM SINH >1965
SELECT empSSN, empName, DAY(empBirthdate) as N'NGÀY SINH', MONTH(empBirthdate) AS N'THÁNG SINH', YEAR(empBirthdate) AS N'NĂM SINH'
FROM tblEmployee
WHERE YEAR(empBirthdate) > 1965
-- 43
SELECT empSSN, empName, FLOOR((DATEDIFF(DAY,empStartdate,getdate())/365.25)) AS N'SỐ NĂM ĐI LÀM', FLOOR((DATEDIFF(DAY,empBirthdate,getdate())/365.25)) AS N'TUỔI'
FROM tblEmployee
WHERE empAddress IN (N'TP. Hồ Chí Minh', 'TP. Hà Nội')
--44
SELECT empSSN, empName, empSalary, FLOOR((DATEDIFF(DAY,empStartdate,getdate())/365.25)) AS N'SỐ NĂM ĐI LÀM', FLOOR((DATEDIFF(DAY,empBirthdate,getdate())/365.25)) AS N'TUỔI'
FROM tblEmployee
WHERE empAddress IN (N'TP. Hồ Chí Minh', 'TP. Hà Nội')
--45
SELECT *
FROM tblEmployee
WHERE FLOOR((DATEDIFF(DAY,empStartdate,getdate())/365.25)) > 5
--46
SELECT empSSN, empName, empSalary, FLOOR((DATEDIFF(DAY,empStartdate,getdate())/365.25)) AS N'SỐ NĂM ĐI LÀM', FLOOR((DATEDIFF(DAY,empBirthdate,getdate())/365.25)) AS N'TUỔI'
FROM tblEmployee
WHERE empAddress IN (N'TP. Hồ Chí Minh', 'TP. Hà Nội')
ORDER BY FLOOR((DATEDIFF(DAY,empStartdate,getdate())/365.25)) ASC, FLOOR((DATEDIFF(DAY,empBirthdate,getdate())/365.25)) DESC
--47
SELECT *
FROM tblEmployee
WHERE empAddress IN (N'TP. Hồ Chí Minh', 'TP. Hà Nội') and empSSN in (
  sElEct dIsTiNCt mgrSSN
  frOm tblDepartment
)
ORDER BY empSalary ASC ,FLOOR((DATEDIFF(DAY,empStartdate,getdate())/365.25)) DESC

select *
from tblEmployee
where empAddress in (N'TP. Hồ Chí Minh', N'TP. Hà Nội') and
 empSSN in (
 select distinct mgrSSN
 from tblDepartment)
Order by empSalary asc, floor((datediff(DAY, empStartdate,getdate())/365.25)) desc