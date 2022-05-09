--Table: Activity
--
--+---------------+---------+
--| Column Name   | Type    |
--+---------------+---------+
--| user_id       | int     |
--| session_id    | int     |
--| activity_date | date    |
--| activity_type | enum    |
--+---------------+---------+
--There is no primary key for this table, it may have duplicate rows.
--The activity_type column is an ENUM of type ('open_session', 'end_session', 'scroll_down', 'send_message').
--The table shows the user activities for a social media website. 
--Note that each session belongs to exactly one user.
-- 
--
--Write an SQL query to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they made at least one activity on that day.
--
--Return the result table in any order.
--
--The query result format is in the following example.
--
-- 
--
--Example 1:
--
--Input: 
--Activity table:
--+---------+------------+---------------+---------------+
--| user_id | session_id | activity_date | activity_type |
--+---------+------------+---------------+---------------+
--| 1       | 1          | 2019-07-20    | open_session  |
--| 1       | 1          | 2019-07-20    | scroll_down   |
--| 1       | 1          | 2019-07-20    | end_session   |
--| 2       | 4          | 2019-07-20    | open_session  |
--| 2       | 4          | 2019-07-21    | send_message  |
--| 2       | 4          | 2019-07-21    | end_session   |
--| 3       | 2          | 2019-07-21    | open_session  |
--| 3       | 2          | 2019-07-21    | send_message  |
--| 3       | 2          | 2019-07-21    | end_session   |
--| 4       | 3          | 2019-06-25    | open_session  |
--| 4       | 3          | 2019-06-25    | end_session   |
--+---------+------------+---------------+---------------+
--Output: 
--+------------+--------------+ 
--| day        | active_users |
--+------------+--------------+ 
--| 2019-07-20 | 2            |
--| 2019-07-21 | 2            |
--+------------+--------------+ 
--Explanation: Note that we do not care about days with zero active users.

select activity_date as day, count(distinct user_id) as active_users from activity
where datediff('2019-07-27', activity_date) < 30
group by 1;

WITH USERS_WITH_DAYS_NON_DUPL AS (
      SELECT DISTINCT USER_ID, ACTIVITY_DATE
        FROM ACTIVITY
       WHERE DATEDIFF('2019-07-27', activity_date) < 30
  )
  SELECT ACTIVITY_DATE AS DAY,
         COUNT(*) AS ACTIVE_USERS
    FROM USERS_WITH_DAYS_NON_DUPL
GROUP BY ACTIVITY_DATE
ORDER BY DAY;

